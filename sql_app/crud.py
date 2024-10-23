from sqlalchemy.orm import Session
from . import models, schemas


################################################################ READ ################################################################

# Retorna o evento de ID especificado:
def get_evento(db: Session, evento_id: int):
    return db.query(models.Evento).filter(models.Evento.id == evento_id).first()


# Retorna o tipo de evento pelo ID específico
def get_tipo(db: Session, tipo_id: int):
    return db.query(models.Tipo).filter(models.Tipo.id == tipo_id).first()


# Retorna o local do evento pelo ID específico
def get_local(db: Session, local_id: int):
    return db.query(models.Local).filter(models.Local.id == local_id).first()


# Retorna o evento de nome especificado, caso não exista nenhum evento com esse nome retorna None
def get_evento_by_nome(db: Session, evento_nome: str):
    return db.query(models.Evento).filter(models.Evento.nome == evento_nome).first()


# Retorna o tipo de nome especificado, caso não exista nenhum tipo com esse nome retorna None
def get_tipo_by_nome(db: Session, tipo_nome: str):
    return db.query(models.Tipo).filter(models.Tipo.nome == tipo_nome).first()


# Retorna o local de nome especificado, caso não exista nenhum local com esse nome retorna None
def get_local_by_nome(db: Session, local_nome: str):
    return db.query(models.Local).filter(models.Local.nome == local_nome).first()


# Retorna todos os eventos armazenados na tabela, com limite e skip
def get_eventos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Evento).offset(skip).limit(limit).all()


# Retorna os tipos armazenados na tabela, com limite e skip
def get_tipos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tipo).offset(skip).limit(limit).all()


# Retorna os locais armazenados na tabela, com limite e skip
def get_locais(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Local).offset(skip).limit(limit).all()


################################################################ CREATE ################################################################


# Cria eventos e adiciona eles na tabela de eventos
def create_evento(db: Session, evento: schemas.EventoCreate):
    db_evento = models.Evento(**evento)
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento


# Cria tipos e adiciona eles na tabela de tipos
def create_tipo(db: Session, tipo: schemas.TipoCreate):
    db_tipo = models.Tipo(**tipo)
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo


# Cria locais e adiciona eles na tabela de locais
def create_local(db: Session, local: schemas.LocalCreate):
    db_local = models.Local(**local)
    db.add(db_local)
    db.commit()
    db.refresh(db_local)
    return db_local


################################################################ UPDATE ################################################################


# Atualiza os dados de um evento que já existe na tabela
def update_evento(db: Session, evento_id: int, evento: schemas.EventoUpdate):
    db_evento = db.query(models.Evento).filter(models.Evento.id == evento_id).first()
    if not db_evento:
        return None

    for key, value in evento.dict(exclude_unset=True).items():
        setattr(db_evento, key, value)

    db.commit()
    db.refresh(db_evento)
    return db_evento


# Atualiza os dados de um tipo que já existe na tabela
def update_tipo(db: Session, tipo_id: int, tipo: schemas.TipoUpdate):
    db_tipo = db.query(models.Tipo).filter(models.Tipo.id == tipo_id).first()
    if not db_tipo:
        return None

    for key, value in tipo.dict(exclude_unset=True).items():
        setattr(db_tipo, key, value)

    db.commit()
    db.refresh(db_tipo)
    return db_tipo


# Atualiza os dados de um local que já existe na tabela
def update_local(db: Session, local_id: int, local: schemas.LocalUpdate):
    db_local = db.query(models.Local).filter(models.Local.id == local_id).first()
    if not db_local:
        return None

    for key, value in local.dict(exclude_unset=True).items():
        setattr(db_local, key, value)

    db.commit()
    db.refresh(db_local)
    return db_local


################################################################ DELETE ################################################################


# Deleta um evento já existente na tabela
def delete_evento(db: Session, evento_id: int):
    db_evento = db.query(models.Evento).filter(models.Evento.id == evento_id).first()
    if not db_evento:
        return None

    db.delete(db_evento)
    db.commit()
    return {"message": "Evento deleted successfully"}


# Deleta um tipo já existente na tabela
def delete_tipo(db: Session, tipo_id: int):
    db_tipo = db.query(models.Tipo).filter(models.Tipo.id == tipo_id).first()
    if not db_tipo:
        return None

    db.delete(db_tipo)
    db.commit()
    return {"message": "Tipo deleted successfully"}


# Deleta um local já existente na tabela
def delete_local(db: Session, local_id: int):
    db_local = db.query(models.Local).filter(models.Local.id == local_id).first()
    if not db_local:
        return None

    db.delete(db_local)
    db.commit()
    return {"message": "Local deleted successfully"}

########################################################################################################################################