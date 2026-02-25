from pydantic import BaseModel

class OrderBase(BaseModel):
    customer_id: int
    product_id: int

class OrderCreate(OrderBase):
    pass       

class OrderResponse(OrderBase):
    id: int

    class Config:
        from_attributes = True
        
