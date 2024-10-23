from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


########## Local ##########
class LocalBase(BaseModel):
    nome: str = Field(
        ...,
        title="Nome do Local",
        description="Nome do local onde o evento será realizado.",
        example="Estádio do Morumbi",
    )
    capacidade: int = Field(
        ...,
        title="Capacidade",
        description="Capacidade máxima de pessoas que o local suporta.",
        example=66795,
    )
    endereco: str = Field(
        ...,
        title="Endereço",
        description="Endereço completo do local.",
        example="Praça Roberto Gomes Pedrosa, 1 - Morumbi, São Paulo - SP, 05653-070",
    )
    telefone: Optional[str] = Field(
        None,
        title="Telefone",
        description="Número de telefone para contato.",
        example="(11) 3749-8000",
    )
    temEstacionamento: bool = Field(
        ...,
        title="Estacionamento",
        description="Se o local tem estacionamento disponível.",
        example=True,
    )
    acessibilidade: bool = Field(
        ...,
        title="Acessibilidade",
        description="Se o local tem facilidades de acessibilidade.",
        example=True,
    )


class LocalCreate(LocalBase):
    pass


class Local(LocalBase):
    id: int = Field(
        ..., title="ID do Local", description="Identificador único do local.", example=1
    )

    class Config:
        from_attributes = True


class LocalUpdate(BaseModel):
    nome: Optional[str] = Field(
        None,
        title="Nome do Local",
        description="Nome do local onde o evento será realizado.",
        example="MorumBis",
    )
    capacidade: Optional[int] = Field(
        None,
        title="Capacidade",
        description="Capacidade máxima de pessoas que o local suporta.",
        example=100,
    )
    endereco: Optional[str] = Field(
        None,
        title="Endereço",
        description="Endereço completo do local.",
        example="Rua X, 123",
    )
    telefone: Optional[str] = Field(
        None,
        title="Telefone",
        description="Número de telefone para contato.",
        example="(11) 1234-5678",
    )
    temEstacionamento: Optional[bool] = Field(
        None,
        title="Estacionamento",
        description="Se o local tem estacionamento disponível.",
        example=True,
    )
    acessibilidade: Optional[bool] = Field(
        None,
        title="Acessibilidade",
        description="Se o local tem facilidades de acessibilidade.",
        example=True,
    )

    class Config:
        from_attributes = True


########## Tipo de Evento ##########
class TipoBase(BaseModel):
    nome: str = Field(
        ...,
        title="Nome do Tipo de Evento",
        description="Nome do tipo de evento.",
        example="Show",
    )
    descricao: str = Field(
        ...,
        title="Descrição do Tipo de Evento",
        description="Uma breve descrição do tipo de evento.",
        example="Apresentação de um artista.",
    )
    publico_alvo: str = Field(
        ...,
        title="Público Alvo",
        description="Público alvo do evento.",
        example="Jovens adultos",
    )
    objetivo: str = Field(
        ...,
        title="Objetivo",
        description="Objetivo principal do evento.",
        example="Entretenimento",
    )
    ehPresencial: bool = Field(
        ...,
        title="Presencial",
        description="Se o evento será realizado de forma presencial.",
        example=True,
    )


class TipoCreate(TipoBase):
    pass


class Tipo(TipoBase):
    id: int = Field(
        ...,
        title="ID do Tipo de Evento",
        description="Identificador único do tipo de evento.",
        example=1,
    )

    class Config:
        from_attributes = True


class TipoUpdate(BaseModel):
    nome: Optional[str] = Field(
        None,
        title="Nome do Tipo de Evento",
        description="Nome do tipo de evento.",
        example="Show",
    )
    descricao: Optional[str] = Field(
        None,
        title="Descrição do Tipo de Evento",
        description="Uma breve descrição do tipo de evento.",
        example="Apresentação de um artista.",
    )
    publico_alvo: Optional[str] = Field(
        None,
        title="Público Alvo",
        description="Público alvo do evento.",
        example="Jovens adultos",
    )
    objetivo: Optional[str] = Field(
        None,
        title="Objetivo",
        description="Objetivo principal do evento.",
        example="Entretenimento",
    )
    ehPresencial: Optional[bool] = Field(
        None,
        title="Presencial",
        description="Se o evento será realizado de forma presencial.",
        example=True,
    )

    class Config:
        from_attributes = True


########## Evento ##########
class EventoBase(BaseModel):
    nome: str = Field(
        ...,
        title="Nome do Evento",
        description="Nome do evento que será realizado.",
        example="Lançamento do Produto X",
    )
    descricao: str = Field(
        ...,
        title="Descrição do Evento",
        description="Uma breve descrição do evento.",
        example="Evento de lançamento do produto X.",
    )
    data: datetime = Field(
        ...,
        title="Data do Evento",
        description="A data e hora em que o evento ocorrerá.",
        example="2021-07-01T18:00:00",
    )
    ehFormal: bool = Field(
        ..., title="Formalidade", description="Se o evento é formal.", example=True
    )
    custoIngresso: int = Field(
        ...,
        title="Custo do Ingresso",
        description="Preço do ingresso para participar do evento.",
        example=150,
    )
    contato: str = Field(
        ...,
        title="Contato",
        description="Informação de contato para o evento.",
        example="contato@evento.com",
    )
    horaInicio: datetime = Field(
        ...,
        title="Hora de Início",
        description="Hora de início do evento.",
        example="2021-07-01T18:00:00",
    )
    horaFim: datetime = Field(
        ...,
        title="Hora de Término",
        description="Hora de término do evento.",
        example="2021-07-01T20:00:00",
    )
    tipo_id: int = Field(
        ...,
        title="ID do Tipo de Evento",
        description="O ID que representa o tipo do evento.",
        example=1,
    )


class EventoCreate(EventoBase):
    local_id: List[int] = Field(
        ...,
        title="IDs dos Locais",
        description="Uma lista de IDs que representam os locais onde o evento será realizado.",
        example=[1, 2, 3],
    )


class Evento(EventoBase):
    id: int = Field(
        ...,
        title="ID do Evento",
        description="Identificador único do evento.",
        example=1,
    )
    locais: List[Local] = Field(
        ...,
        title="Locais",
        description="Locais onde o evento será realizado.",
        example=[
            {
                "id": 1,
                "nome": "MorumBis",
                "endereco": "Rua X, 123",
                "capacidade": 100,
                "telefone": "(11) 1234-5678",
                "temEstacionamento": True,
                "acessibilidade": True,
            }
        ],
    )

    class Config:
        from_attributes = True


class EventoUpdate(BaseModel):
    nome: Optional[str] = Field(
        None,
        title="Nome do Evento",
        description="Nome do evento que será realizado.",
        example="Lançamento do Produto X",
    )
    descricao: Optional[str] = Field(
        None,
        title="Descrição do Evento",
        description="Uma breve descrição do evento.",
        example="Evento de lançamento do produto X.",
    )
    data: Optional[datetime] = Field(
        None,
        title="Data do Evento",
        description="A data e hora em que o evento ocorrerá.",
        example="2021-07-01T18:00:00",
    )
    ehFormal: Optional[bool] = Field(
        None, title="Formalidade", description="Se o evento é formal.", example=True
    )
    custoIngresso: Optional[int] = Field(
        None,
        title="Custo do Ingresso",
        description="Preço do ingresso para participar do evento.",
        example=150,
    )
    contato: Optional[str] = Field(
        None,
        title="Contato",
        description="Informação de contato para o evento.",
        example="contato@evento.com",
    )
    horaInicio: Optional[datetime] = Field(
        None,
        title="Hora de Início",
        description="Hora de início do evento.",
        example="2021-07-01T18:00:00",
    )
    horaFim: Optional[datetime] = Field(
        None,
        title="Hora de Término",
        description="Hora de término do evento.",
        example="2021-07-01T20:00:00",
    )
    tipo_id: Optional[int] = Field(
        None,
        title="ID do Tipo de Evento",
        description="O ID que representa o tipo do evento.",
        example=1,
    )
    local_id: Optional[List[int]] = Field(
        None,
        title="IDs dos Locais",
        description="Uma lista de IDs que representam os locais onde o evento será realizado.",
        example=[1, 2, 3],
    )

    class Config:
        from_attributes = True
