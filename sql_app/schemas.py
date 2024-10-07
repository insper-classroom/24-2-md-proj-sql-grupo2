from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    hashed_password: str
    is_active: bool
    items: list[Item] = []

    class Config:
        from_attributes = True
class EventoBase(BaseModel):
    nome: str
    data: str
    hora: str
    local_id: list[int]
    tipo_id: list[int]
class EventoCreate(EventoBase):
    pass
class Evento(EventoBase):
    id: int
    class Config:
        from_attributes = True
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
