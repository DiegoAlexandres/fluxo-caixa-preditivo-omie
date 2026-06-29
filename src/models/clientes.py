from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from ..database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    razao_social = Column(String, nullable=True)
    cpf_cnpj = Column(String, nullable=True)


class ClienteBase(BaseModel):
    nome: str
    razao_social: str | None = None
    cpf_cnpj: str | None = None


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(BaseModel):
    nome: str | None = None
    razao_social: str | None = None
    cpf_cnpj: str | None = None


class ClienteOut(ClienteBase):
    id: int

    class Config:
        from_attributes = True
