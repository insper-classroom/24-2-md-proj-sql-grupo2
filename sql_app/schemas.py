from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


########## Local ##########
class LocalBase(BaseModel):
    nome: str
    capacidade: int
    endereco: str
    telefone: Optional[str] = None
    temEstacionamento: bool
    acessibilidade: bool


class LocalCreate(LocalBase):
    pass


class Local(LocalBase):
    id: int

    class Config:
        from_attributes = True


class LocalUpdate(BaseModel):
    nome: Optional[str] = None
    capacidade: Optional[int] = None
    endereco: Optional[str] = None
    telefone: Optional[str] = None
    temEstacionamento: Optional[bool] = None
    acessibilidade: Optional[bool] = None

    class Config:
        from_attributes = True


########## Tipo de Evento ##########
class TipoBase(BaseModel):
    nome: str
    descricao: str
    publico_alvo: str
    objetivo: str
    ehPresencial: bool


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
    ehPresencial: Optional[bool] = None

    class Config:
        from_attributes = True


########## Evento ##########
class EventoBase(BaseModel):
    nome: str
    descricao: str
    data: datetime
    ehFormal: bool
    custoIngresso: int
    contato: str
    horaInicio: datetime
    horaFim: datetime
    tipo_id: int


class EventoCreate(EventoBase):
    local_id: List[int]


class Evento(EventoBase):
    id: int
    locais: List[Local]

    class Config:
        from_attributes = True


class EventoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    data: Optional[datetime] = None
    ehFormal: Optional[bool] = None
    custoIngresso: Optional[int] = None
    contato: Optional[str] = None
    horaInicio: Optional[datetime] = None
    horaFim: Optional[datetime] = None
    tipo_id: Optional[int] = None
    local_id: Optional[List[int]] = None

    class Config:
        from_attributes = True
