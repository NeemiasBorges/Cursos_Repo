from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from typing import List,Optional

from models import Curso
app = FastAPI()

cursos = {
    1: {
        "titulo": "Titulo teste",
        "aulas": 111,
        "horas": 11
    },
    2: {
        "titulo": "teste dois",
        "aulas": 2,
        "horas": 22
    }
}

@app.get('/')
async def root():
    return ""

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_cursos(curso_id: int):
    try:
        curso = cursos[curso_id]
        curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso Nao Encontrado.')

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_cursos(curso: Optional[Curso] = None):
    try:
        if  curso.id not in cursos:
            curso.id = len(cursos) + 1
            cursos[curso.id] = curso
            return cursos
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Já existe um curso com ID {curso.id}. ")
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Entitdade invalida"
        )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)