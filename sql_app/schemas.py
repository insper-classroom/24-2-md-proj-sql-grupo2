from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, time

########## Evento ##########
# Modelo base para os dados de evento
class EventoBase(BaseModel):
    nome: str = Field(title="nome", description="Nome do evento", example="Tech Talk")
    descricao: str = Field(
        title="descricao",
        description="Descrição do evento",
        example="Discussões sobre tendências tecnológicas",
    )
    data: date = Field(
        title="data", description="Data de início do evento", example="2024-11-15"
    )
    ehFormal: bool = Field(
        title="ehFormal", description="O evento é formal ou não", example=True
    )
    custoIngresso: int = Field(
        title="custoIngresso",
        description="Preço do ticket médio do ingresso",
        example=100,
    )
    contato: str = Field(
        title="contato", description="Contato do email", example="(11) 96590-1234"
    )
    horaInicio: time = Field(
        title="horaInicio", description="Horário de início do evento", example="10:00"
    )
    horaFim: time = Field(
        title="horaFim", description="Horário de fim do evento", example="12:00"
    )
    local_id: list[int] = Field(
        title="local_id",
        description="IDs dos locais em que o evento vai ocorrer",
        example=[1, 2, 3],
    )
    tipo_id: int = Field(title="tipo_id", description="ID do tipo de evento", example=1)

# Modelo para criação de um novo evento, que herda de EventoBase
class EventoCreate(EventoBase):
    pass

# Modelo para representar um evento completo, com o campo 'id' incluído
class Evento(EventoBase):
    id: int

    # Configuração para permitir mapeamento de atributos diretamente de um ORM
    class Config:
        from_attributes = True

# Modelo para atualizar um evento, com todos os campos opcionais
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
    tipo_id: Optional[int] = None

########## Tipo ##########
# Modelo base para os dados de tipo de evento
class TipoBase(BaseModel):
    nome: str = Field(
        title="nome", description="Nome do tipo de evento", example="Palestra"
    )
    descricao: str = Field(
        title="descricao",
        description="Descrição do tipo de evento",
        example="Evento de caráter informativo com apresentação de palestrantes",
    )
    publico_alvo: str = Field(
        title="publico_alvo",
        description="Público alvo do tipo de evento",
        example="Profissionais de tecnologia",
    )
    objetivo: str = Field(
        title="objetivo",
        description="Objetivo do tipo de evento",
        example="Disseminar conhecimento tecnológico",
    )
    ehPresencial: bool = Field(
        title="ehPresencial",
        description="Indica se o evento é presencial ou não",
        example=True,
    )

# Modelo para criação de um novo tipo de evento, que herda de TipoBase
class TipoCreate(TipoBase):
    pass

# Modelo para representar um tipo de evento completo, com o campo 'id' incluído
class Tipo(TipoBase):
    id: int

    # Configuração para permitir mapeamento de atributos diretamente de um ORM
    class Config:
        from_attributes = True

# Modelo para atualizar um tipo de evento, com todos os campos opcionais
class TipoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    publico_alvo: Optional[str] = None
    objetivo: Optional[str] = None
    ehPresencial: Optional[int] = None

########## Local ##########
# Modelo base para os dados de um local de evento
class LocalBase(BaseModel):
    nome: str = Field(
        title="nome", description="Nome do local", example="Centro de Convenções"
    )
    endereco: str = Field(
        title="endereco", description="Endereço do local", example="Rua dos Bobos, 0"
    )
    capacidade: int = Field(
        title="capacidade", description="Capacidade máxima do local", example=100
    )
    telefone: str = Field(
        title="telefone",
        description="Número de telefone do local",
        example="(11) 1234-5678",
    )
    temEstacionamento: bool = Field(
        title="temEstacionamento",
        description="Indica se o local possui estacionamento",
        example=True,
    )
    acessibilidade: bool = Field(
        title="acessibilidade",
        description="Indica se o local possui acessibilidade",
        example=True,
    )
    event_id: list[int] = Field(
        title="event_id",
        description="IDs dos eventos que ocorrem neste local",
        example=[1, 2, 3],
    )

# Modelo para criação de um novo local, que herda de LocalBase
class LocalCreate(LocalBase):
    pass

# Modelo para representar um local completo, com o campo 'id' incluído
class Local(LocalBase):
    id: int

    # Configuração para permitir mapeamento de atributos diretamente de um ORM
    class Config:
        from_attributes = True

# Modelo para atualizar um local, com todos os campos opcionais
class LocalUpdate(BaseModel):
    nome: Optional[str] = None
    endereco: Optional[str] = None
    capacidade: Optional[int] = None
    telefone: Optional[str] = None
    temEstacionamento: Optional[bool] = None
    acessibilidade: Optional[bool] = None
    event_id: Optional[list[int]] = None
