from fastapi import FastAPI
from app.core.database import engine, Base
from app.controllers.product_controller import router as product_router

app = FastAPI(title="E-commerce API")

#Create tables automatically
Base.metadata.create_all(bind=engine)

#Register routers
app.include_router(product_router)