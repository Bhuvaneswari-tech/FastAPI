from pydantic import BaseModel, Field
from typing import Optional

#used to creating a product
class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = Field(None)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    
#used when return a product data
class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    stock: int

    class Config:
        from_attributes = True