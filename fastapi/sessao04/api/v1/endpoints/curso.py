from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession 
from sqlalchemy.future import select

from models.curso_models import CursoModel
from schemas.curso_schemas import CursoSchema
from core.deps import get_session

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoSchema)
async def post_curso(curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    novo_curso = CursoModel(titulo = curso.titulo, aulas=curso.aulas, horas = curso.horas)

    db.add(novo_curso)
    await db.commit()

    return novo_curso


@router.get('/', response_model=List[CursoSchema])
async def post_curso(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)  
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()    
        return cursos
    
@router.get('/{curso_id}', response_model=CursoSchema, status_code=status.HTTP_200_OK)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).where(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso = result.scalar_one()

        if curso:    
            return curso
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

@router.put('/{curso_id}', response_model=CursoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).where(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_db = result.scalar_one()

        if curso_db:
            curso_db.titulo = curso.titulo
            curso_db.aulas = curso.aulas
            curso_db.horas = curso.horas

            await db.commit()
            return curso_db
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
        

@router.delete('/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).where(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso = result.scalar_one()

        if curso:
            db.delete(curso)
            await db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
        
        