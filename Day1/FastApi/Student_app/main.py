from fastapi import FastAPI

#create FastAPI app instance
app = FastAPI()

# Define a route for the root URL
@app.get("/")
def read_root():
    return {"message": "Welcome to the Student API!"}       

#student endpoint
@app.get("/student")
def get_student():
    student = {
        "name": "Alice",
        "age": 22,
        "courses": ["Math", "Science"],
        "is_graduated": False
    }
    return student