from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from bson import ObjectId
from app.services.mongo_client import get_policy_collection
from app.services.rag import RagService
from app.services.recommendation import build_recommendations
from app.api.auth import current_user

router = APIRouter()
rag = RagService()


class SearchPayload(BaseModel):
    query: Optional[str] = None
    category: Optional[str] = None
    state: Optional[str] = None
    age_group: Optional[str] = None
    income_bracket: Optional[str] = None
    ministry: Optional[str] = None
    deadline: Optional[str] = None
    tags: List[str] = []
    page: int = 1
    limit: int = 20


@router.post("/search")
async def search_policies(payload: SearchPayload, user: dict = Depends(current_user)):
    collection = get_policy_collection()
    query = {k: v for k, v in payload.dict().items() if v and k not in ["page", "limit", "query", "tags"]}
    filters = [{"category": payload.category}] if payload.category else []
    if payload.state:
        query["state_applicability"] = payload.state
    if payload.tags:
        query["tags"] = {"$all": payload.tags}

    results = []
    if payload.query:
        results = rag.search_with_rag(payload.query, filters=query)
    else:
        cursor = collection.find(query).skip((payload.page - 1) * payload.limit).limit(payload.limit)
        results = [doc for doc in await cursor.to_list(length=payload.limit)]

    return {"count": len(results), "results": results}


@router.get("/{policy_id}")
async def get_policy(policy_id: str, user: dict = Depends(current_user)):
    collection = get_policy_collection()
    policy = await collection.find_one({"_id": ObjectId(policy_id)})
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    recommendations = build_recommendations(policy, user)
    return {"policy": policy, "recommendations": recommendations}


@router.post("/suggestions")
async def suggestions(profile: dict, user: dict = Depends(current_user)):
    collection = get_policy_collection()
    recommendations = build_recommendations(profile, user)
    return {"recommendations": recommendations}
