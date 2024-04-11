from src.core.pydantic_model import BaseModel

class ResponseBase(BaseModel):
    pass

    class Config:
        extra = 'forbid'
        orm_mode = True