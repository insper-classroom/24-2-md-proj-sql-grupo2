# Arquivo para a criação dos schemas das estruturas que serão usadas

from pydantic import BaseModel
from typing import Optional
from datetime import date, time


class EventoBase(BaseModel):
    nome: str
    descricao: str
    data: date
    ehFormal: bool
    custoIngresso: int
    contato: str
    horaInicio: time
    horaFim: time
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
    descricao: Optional[str] = None
    data: Optional[date] = None
    ehFormal: Optional[bool] = None
    custoIngresso: Optional[int] = None
    contato: Optional[str] = None
    horaInicio: Optional[time] = None
    horaFim: Optional[time] = None
    local_id: Optional[list[int]] = None
    tipo_id: Optional[list[int]] = None


class TipoBase(BaseModel):
    nome: str
    descricao: str
    publico_alvo: str
    objetivo: str
    ehPresencial: int


class TipoCreate(TipoBase):
    pass


class Tipo(TipoBase):
    id: int

    class Config:
        from_attributes = True


class TipoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    publico_alvo: Optional[str] = None
    objetivo: Optional[str] = None
    ehPresencial: Optional[int] = None


class LocalBase(BaseModel):
    nome: str
    endereco: str
    capacidade: int
    telefone: str
    temEstacionamento: bool
    acessibilidade: bool
    event_id: list[int]


class LocalCreate(LocalBase):
    pass


class Local(LocalBase):
    id: int

    class Config:
        from_attributes = True


class LocalUpdate(BaseModel):
    nome: Optional[str] = None
    endereco: Optional[str] = None
    capacidade: Optional[int] = None
    telefone: Optional[str] = None
    temEstacionamento: Optional[bool] = None
    acessibilidade: Optional[bool] = None
    event_id: Optional[list[int]] = None
