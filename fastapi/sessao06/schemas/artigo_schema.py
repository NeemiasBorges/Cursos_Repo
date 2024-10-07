from typing import Optional

from pydantic import BaseModel, HttpUrl

class ArtigoSchemas(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    url_fonte: Optional[HttpUrl] = None
    usuario_id: Optional[int]

    class Config:
        from_attributes = True
