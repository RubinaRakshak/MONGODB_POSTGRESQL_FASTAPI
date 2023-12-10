from pydantic import BaseModel


class CreateJobRequest(BaseModel):
    name: str
    email: str
    password: str
    phone: str
    