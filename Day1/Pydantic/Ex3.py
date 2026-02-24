#Field Validation & Constraints

from pydantic import BaseModel, ValidationError, Field

class Product(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    price: float = Field(..., gt=0)  # price must be greater than 0
    stock: int = Field(..., ge=0)   # stock must be greater than or equal to 0
    
#valid input
try:
    product = Product(name="Laptop", price=55000, stock=10)
    print("Valid Product Created:")
    print(product)
    print("\nAs Dictionary:")
    print(product.model_dump())
except ValidationError as e:
    print("Validation error:", e)   

#invalid input
try:
    product = Product(name="TV", price=-5000, stock=-5)
    print(product.dict())
except ValidationError as e:    
    print("Validation error:", e)


