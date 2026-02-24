import json

with open("user.json", "r") as file:
    data = json.load(file)

print(data["name"]+" is from "+data["city"])
#print(data["age"])
print(data["age"]+5)
print(data["name"]+" Visweswaran")