# Arquivo para a criação dos schemas das estruturas que serão usadas

from pydantic import BaseModel
from typing import Optional
from datetime import date


class EventoBase(BaseModel):
    nome: str
    data: date
    local_id: list[int]
    tipo_id: list[int]


class EventoCreate(EventoBase):
    pass


class Evento(EventoBase):
    id: int

    class Config:
        from_attributes = True


class EventoUpdate(BaseModel):
    nome: Optional[str] = None
    data: Optional[date] = None
    local_id: Optional[list[int]] = None
    tipo_id: Optional[list[int]] = None


class TipoBase(BaseModel):
    nome: str
    descricao: str
    publico_alvo: str
    evento_id: list[int]


class TipoCreate(TipoBase):
    pass


class Tipo(TipoBase):
    id: int
    evento_id: list[int]

    class Config:
        from_attributes = True


class TipoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    publico_alvo: Optional[str] = None
    evento_id: Optional[list[int]] = None


class LocalBase(BaseModel):
    nome: str
    endereco: str
    capacidade: int
    evento_id: list[int]


class LocalCreate(LocalBase):
    pass


class Local(LocalBase):
    id: int
    evento_id: list[int]

    class Config:
        from_attributes = True


class LocalUpdate(BaseModel):
    nome: Optional[str] = None
    endereco: Optional[str] = None
    capacidade: Optional[int] = None
    evento_id: Optional[list[int]] = None
