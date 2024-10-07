from fastapi import FastAPI

from core.configs import settings   
from api.api import api_router

app = FastAPI(title="API de Cursos", version="0.1.0")   
app.include_router(api_router, prefix=settings.AP_V1_STR)

if __name__ ==  '__main__':
    import uvicorn
    uvicorn.run('main:app',host="0.0.0.0", port=8000, reload=True)