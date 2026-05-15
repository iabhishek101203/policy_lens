from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
from datetime import date


class PolicyBase(BaseModel):
    title: str
    ministry: str
    category: str
    state_applicability: List[str] = []
    eligibility: Optional[str] = None
    benefits: Optional[str] = None
    required_documents: Optional[str] = None
    application_process: Optional[str] = None
    deadline: Optional[str] = None
    official_link: Optional[HttpUrl] = None
    target_audience: Optional[str] = None
    summary: Optional[str] = None
    tags: List[str] = []
    source: Optional[str] = None
    faqs: List[str] = []
    published_date: Optional[date] = None


class PolicyCreate(PolicyBase):
    pass


class PolicyInDB(PolicyBase):
    id: str = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "title": "National Scholarship Scheme",
                "ministry": "Ministry of Education",
                "category": "Education",
                "state_applicability": ["All"],
                "eligibility": "Students with household income below threshold.",
                "benefits": "Tuition fee waiver, stipend support.",
                "official_link": "https://example.gov/policy/123",
            }
        }
