from typing import List
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession 
from sqlmodel import select

from models.curso_model import CursoModel
from core.deps import get_session

from sqlmodel.sql.expression import Select,SelectOfScalar

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

router = APIRouter()    

@router.post("/", status_code=status.HTTP_201_CREATED,response_model=CursoModel)
async def post_cursp(curso: CursoModel,db: AsyncSession = Depends(get_session)):
    novo_curso = CursoModel(titulo=curso.titulo,descricao=curso.descricao, horas=curso.horas, aulas=curso.aulas)    

    db.add(novo_curso)
    await db.commit()

    return novo_curso
    
@router.get("/cursos", response_model=List[CursoModel])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    cursos = await db.execute(select(CursoModel))
    return cursos.scalars().all()


@router.get("/{curso_id}", response_model=CursoModel)
async def get_curso(curso_id: int,db: AsyncSession = Depends(get_session)):
    curso = await db.get(CursoModel, curso_id)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return curso

