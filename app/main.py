from app.api import submission_routes
from contextlib import asynccontextmanager
from fastapi import FastAPI
@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Server is running")
    yield
    print("Server shutdown")
app=FastAPI(lifespan=lifespan)
# add all router
app.include_router(submission_routes.router)
@app.get("/")
async def root():
    return {"message":"Server is runnig"}