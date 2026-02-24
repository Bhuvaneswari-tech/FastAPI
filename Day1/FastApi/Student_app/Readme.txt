Create virtual environment

pip install fastapi uvicorn

to Run the application

uvicorn main:app --reload

What is FastApi?
Used to create Rest APIs
it supports automatic Validation
its very fast
it generates swagger docs
FastApi helps to build APIs in python with less code and high performance

Why do we use uvicorn?
its a server used to run FastAPI app
FastAPI creates the app
uvicorn runs the app
its an ASGI server
its fast and lightweight
uvicorn is the engine that runs the fastAPI app

What is ASGI?
ASGI - Asynchronous Server Gateway Interface
It is a standard for python web servers
it supports async programming
it allows handling multiple requests at that same time
ASGI allows FastAPI to handle multiple users effectively using async

What does --reload do?
Automatically restart the server when code changes
useful during development
Not recommended in production
--reload restarts the server automatically whenever we save changes in the code.

Why use Optional[str] in query parameters?
Because the parameter is not mandatory. If the client does not provide it, 
FastAPI assigns None. Optional[str] clearly indicates that the variable can be 
either a string or None.
