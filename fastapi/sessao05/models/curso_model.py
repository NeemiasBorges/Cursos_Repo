from typing import Optional
from sqlmodel import Field, SQLModel

class CursoModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    aulas: int
    horas: int