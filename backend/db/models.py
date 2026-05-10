import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ImageJob(Base):
    __tablename__ = "image_jobs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    status = Column(String, default="pending")

    original_image_url = Column(String, nullable=True)

    extracted_keywords = Column(JSONB, nullable=True)
    results = Column(JSONB, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())