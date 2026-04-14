
from typing import Any, Dict, Optional
import uuid
from sqlmodel import JSON, SQLModel,Field
from sqlalchemy import Column


class FinancialSubmissionModel(SQLModel, table=True):
    id:uuid.UUID=Field(
        default_factory=uuid.uuid4,
        primary_key=True, 
        index=True)
    file_name:str | None = None
    file_type:str | None = None
    file_url:str
    status:str
    extracted_data: Optional[Dict[str, Any]] = Field(default=None, sa_column=Column(JSON))
    created_at: Optional[str] = None
    