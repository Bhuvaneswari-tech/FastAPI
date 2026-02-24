from pydantic import BaseModel, ValidationError
from typing import List
import json

#Address Model
class Address(BaseModel):
    city: str
    zip_code: str

#User Model with nested Address
class User(BaseModel):  
    id: int
    name: str
    age: int
    email: str
    address: List[Address]

#JSON Input:
json_input = '''
{
  "id": 1,
  "name": "Bhuvana",
  "age": 30,
  "email": "bhuvana@example.com",
  "address": [
    {"city": "Chennai", "zip_code": "600001"}
  ]
}
'''

try:
    #json.loads()   → JSON string  →  Python dict
    data = json.loads(json_input)
    
    #validate using pydantic
    user = User(**data)
    
    #print the validated data
    print("Validated User:", user)
    
    print("\n Accessing nested data:")
    for address in user.address:
        print(f"City: {address.city}, Zip Code: {address.zip_code}")
    
    print("\n Accessing specific nested field:")
    print(user.address[0].city)  # Accessing city of the first address
    
except ValidationError as e:
    print("Validation error:", e)