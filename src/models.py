from datetime import date
from enum import Enum
from pydantic import BaseModel


class TipoConta(str, Enum):
    PAGAR = "pagar"
    RECEBER = "receber"


class ContaBase(BaseModel):
    nome: str
    valor: float
    data: date
    tipo: TipoConta


class Conta(ContaBase):
    id: int


class DiaProjetado(BaseModel):
    data: date
    movimento_do_dia: float
    saldo_acumulado: float
