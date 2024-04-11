from src.core.pydantic_model import BaseModel

class RequestHeaderModel(BaseModel):
    class Config:
        extra = 'forbid'