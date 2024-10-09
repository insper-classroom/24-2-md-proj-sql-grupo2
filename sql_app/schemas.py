# Arquivo para a criação dos schemas das estruturas que serão usadas

from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, time


class EventoBase(BaseModel):
    nome: str = Field(title ="nome",description = "Nome do evento" ,example="Tech Talk")
    descricao: str = Field(title = "descricao",description ="Descrição do evento" ,example="Discussões sobre tendências tecnológicas")
    data: date = Field(title ="data",description = "Data de ínico do evento"  ,example="2024-11-15")
    ehFormal: bool = Field(title ="ehFormal", description = "O evento é formal ou não" ,example=True)
    custoIngresso: int = Field(title = "custoIngresso",description ="Preço do ticket medio do ingresso" ,example=100)
    contato: str = Field(title ="contato",description ="Contato do email" ,example="(11) 96590-1234")
    horaInicio: time = Field(title = "horaInicio",description = "Horário de início do evento" ,example="10:00")
    horaFim: time = Field(title ="horaFim",description = "Horário de fim do evento", example="12:00")
    local_id: list[int] = Field(title ="local_id",description = "Locais em que o evento vai ocorrer" ,example=[1, 2, 3])
    tipo_id: list[int] = Field(title = "tipo_id",description = "do evento ", example=[1, 2, 3])


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
    nome: str = Field(
        title="nome",
        description="Nome do tipo de evento",
        example="Palestra"
    )
    descricao: str = Field(
        title="descricao",
        description="Descrição do tipo de evento",
        example="Evento de caráter informativo com apresentação de palestrantes"
    )
    publico_alvo: str = Field(
        title="publico_alvo",
        description="Público alvo do tipo de evento",
        example="Profissionais de tecnologia"
    )
    objetivo: str = Field(
        title="objetivo",
        description="Objetivo do tipo de evento",
        example="Disseminar conhecimento tecnológico"
    )
    ehPresencial: bool = Field(
        title="ehPresencial",
        description="Indica se o evento é presencial ou não",
        example=True
    )


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
    nome: str = Field(
        title="nome",
        description="Nome do local",
        example="Centro de Convenções"
    )
    endereco: str = Field(
        title="endereco",
        description="Endereço do local",
        example="Rua dos Bobos, 0"
    )
    capacidade: int = Field(
        title="capacidade",
        description="Capacidade máxima do local",
        example=100
    )
    telefone: str = Field(
        title="telefone",
        description="Número de telefone do local",
        example="(11) 1234-5678"
    )
    temEstacionamento: bool = Field(
        title="temEstacionamento",
        description="Indica se o local possui estacionamento",
        example=True
    )
    acessibilidade: bool = Field(
        title="acessibilidade",
        description="Indica se o local é acessível",
        example=True
    )
    event_id: list[int] = Field(
        title="event_id",
        description="IDs dos eventos que ocorrem neste local",
        example=[1, 2, 3]
    )
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
