from pydantic import BaseModel


class ComplaintRequest(BaseModel):
    citizen_name: str
    complaint: str


class ComplaintResponse(BaseModel):
    id: int
    citizen_name: str
    complaint: str

    class Config:
        from_attributes = True