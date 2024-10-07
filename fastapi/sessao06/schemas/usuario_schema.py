from typing import Optional
from typing import List

from pydantic import BaseModel, EmailStr
from schemas.artigo_schema import ArtigoSchemas

class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: Optional[bool] = False

    class Config:
        from_attributes = True

class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str

class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchemas]] = []

class UsuarioSchemaUp(UsuarioSchemaBase):
       nome: Optional[str] = None
       sobrenome: Optional[str] = None
       email: Optional[EmailStr]
       senha: Optional[str] = None
       eh_admin: Optional[bool] = False