from fastapi import APIRouter

from api.v1.endpoints import usuario, artigo


api_router = APIRouter()

api_router.include_router(usuario.router, prefix='/usuarios', tags=['usuarios'])
api_router.include_router(artigo.router, prefix='/artigos', tags=['artigos'])