from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.artigo_model import ArtigoModel
from models.usuario_model import UsuarioModel
from schemas.artigo_schema import ArtigoSchemas
from core.deps import  get_current_user, get_session

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ArtigoSchemas)
async def post_artigo(artigo: ArtigoSchemas, usuario_logado:UsuarioModel = Depends(get_current_user) ,
     db: AsyncSession = Depends(get_session)):
    
    novo_artigo = ArtigoModel(titulo= artigo.titulo,
        descricao=artigo.descricao,
        url_fonte=artigo.url_fonte,
        usuario_id=usuario_logado.id)
    
    db.add(novo_artigo)
    await db.commit()
    return novo_artigo


@router.get('/', response_model=List[ArtigoSchemas])
async def get_artigos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ArtigoModel)
        retult = await session.execute(query)
        artigos: List[ArtigoModel] = retult.scalars().all()

        return artigos

@router.get('/{artigo_id}', response_model=ArtigoSchemas, status_code=status.HTTP_200_OK)
async def get_artigo(artigo_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ArtigoModel).where(ArtigoModel.id == artigo_id)
        result = await session.execute(query)
        artigo = result.scalars().unique().one_or_none()

        if artigo:
            return artigo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Artigo não encontrado')


@router.put('/{artigo_id}', response_model=ArtigoSchemas, status_code=status.HTTP_200_OK)
async def put_artigo(artigo_id: int, artigo: ArtigoSchemas, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ArtigoModel).where(ArtigoModel.id == artigo_id)
        result = await session.execute(query)
        artigo_db = result.scalars().unique().one_or_none()

        if artigo_db:
            for key, value in artigo.dict(exclude_unset=True).items():
                setattr(artigo_db, key, value)
            await db.commit()
            return artigo_db
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Artigo não encontrado')
    

@router.delete('/{artigo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_artigo(artigo_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ArtigoModel).where(ArtigoModel.id == artigo_id)
        result = await session.execute(query)
        artigo = result.scalars().unique().one_or_none()

        if artigo:
            await session.delete(artigo)
            await db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Artigo não encontrado')
    
