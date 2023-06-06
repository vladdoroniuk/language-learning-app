from fastapi import FastAPI
from fastapi.routing import APIRouter
from users.users_controller import router as users_router
from database import init_db

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


api_router = APIRouter(prefix="/api")
api_router.include_router(users_router, prefix="/users")
app.include_router(api_router)
