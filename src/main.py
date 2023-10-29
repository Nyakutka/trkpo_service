from fastapi import FastAPI

from src.routes.routes import router

app = FastAPI(debug=True)  # TODO: remove debug after release
app.include_router(router=router)
