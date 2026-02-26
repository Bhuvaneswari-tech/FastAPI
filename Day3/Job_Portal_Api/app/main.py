from fastapi import FastAPI
from app.routers import auth_router, job_router
from app.database import Base, engine

#create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Portal API with JWT and RBAC")

app.include_router(auth_router.router)
app.include_router(job_router.router)
