from fastapi import APIRouter, HTTPException, Depends
from app.services.scraper import PolicyScraper
from app.services.mongo_client import get_policy_collection
from app.api.auth import current_user
from bson import ObjectId

router = APIRouter()


def require_admin(user: dict = Depends(current_user)):
    if not user.get("admin", False):
        raise HTTPException(status_code=403, detail="Admin access required")
    return user


@router.post("/scrape")
def run_scraper(user: dict = Depends(require_admin)):
    scraper = PolicyScraper()
    report = scraper.run_scrape()
    return {"status": "scrape_started", "report": report}


@router.get("/policies")
async def list_policies(user: dict = Depends(require_admin)):
    collection = get_policy_collection()
    docs = await collection.find().limit(200).to_list(length=200)
    return {"count": len(docs), "policies": docs}


@router.delete("/policies/{policy_id}")
async def delete_policy(policy_id: str, user: dict = Depends(require_admin)):
    collection = get_policy_collection()
    result = await collection.delete_one({"_id": ObjectId(policy_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Policy not found")
    return {"deleted": policy_id}
