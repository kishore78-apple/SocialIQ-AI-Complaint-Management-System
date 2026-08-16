from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from database import Base


class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)

    customer_name = Column(String)

    email = Column(String)

    phone = Column(String)

    complaint = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    complaint_id = Column(Integer, nullable=False)

    department = Column(String(100))

    priority = Column(String(50))

    sentiment = Column(String(50))

    emergency = Column(String(50))

    harmful = Column(String(50))

    feedback_category = Column(String(100))

    government_action = Column(String(200))

    created_at = Column(DateTime(timezone=True), server_default=func.now())