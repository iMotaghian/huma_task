from pydantic import BaseModel,Field

class LogCreateSchema(BaseModel):
    client_id : str = Field(..., description="User client ID")
    message : str = Field(...,description="User Message")
