from sqlalchemy import Column, Integer, String, ForeignKey,Boolean , VARCHAR
from sqlalchemy.orm import relationship

from core.configs import settings

class ArtigoModel(settings.DBBaseModel):
    __tablename__ = 'artigos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(254))
    url_fonte = Column(String(254))
    descricao = Column(String(254))
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    criador= relationship('UsuarioModel', back_populates='artigos', lazy='joined')