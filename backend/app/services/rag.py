import os
from typing import List, Dict, Optional
import chromadb
from chromadb.config import Settings as ChromaSettings
from chromadb.utils import embedding_functions
from app.core.config import settings
from app.core.logging import logger


class RagService:
    def __init__(self):
        api_key = settings.openai_api_key or os.getenv("OPENAI_API_KEY")
        self.client = chromadb.Client(
            ChromaSettings(chroma_db_impl="duckdb+parquet", persist_directory=settings.chroma_persist_directory)
        )
        self.embedding_function = embedding_functions.OpenAIEmbeddingFunction(
            api_key=api_key,
            model_name="text-embedding-3-large",
        )
        self.collection = self.client.get_or_create_collection(
            name="policy_embeddings",
            embedding_function=self.embedding_function,
        )

    def ingest_documents(self, policies: List[Dict]):
        ids = [str(policy.get("_id") or policy.get("title")) for policy in policies]
        documents = [self.build_document(policy) for policy in policies]
        metadatas = [{
            "title": policy.get("title"),
            "category": policy.get("category"),
            "ministry": policy.get("ministry"),
            "source": policy.get("source"),
        } for policy in policies]
        self.collection.add(ids=ids, documents=documents, metadatas=metadatas)
        self.client.persist()
        logger.info("Ingested %d documents into RAG store", len(policies))

    def build_document(self, policy: Dict) -> str:
        fields = [
            f"Title: {policy.get('title', '')}",
            f"Ministry: {policy.get('ministry', '')}",
            f"Category: {policy.get('category', '')}",
            f"Eligibility: {policy.get('eligibility', '')}",
            f"Benefits: {policy.get('benefits', '')}",
            f"Documents: {policy.get('required_documents', '')}",
            f"Application: {policy.get('application_process', '')}",
            f"Deadline: {policy.get('deadline', '')}",
            f"Link: {policy.get('official_link', '')}",
        ]
        return "\n".join(item for item in fields if item)

    def search_with_rag(self, query: str, filters: Optional[Dict] = None, limit: int = 8) -> List[Dict]:
        query_filters = {k: v for k, v in (filters or {}).items() if v is not None}
        results = self.collection.query(
            query_texts=[query],
            n_results=limit,
            where=query_filters if query_filters else None,
        )
        response = []
        for ids, docs, metas, distances in zip(results["ids"], results["documents"], results["metadatas"], results["distances"]):
            for _id, doc, meta, distance in zip(ids, docs, metas, distances):
                response.append({"id": _id, "document": doc, "metadata": meta, "score": float(distance)})
        return response
