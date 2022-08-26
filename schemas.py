from pydantic import BaseModel

# Create Item Schema (Pydantic Model)
class Item(BaseModel):
    task:str
    #rating:int

# Complete students Schema (Pydantic Model)
class Stu(BaseModel):
    id: int
    task: str

    class Config:
        orm_mode = True