# dicionários para armazenar dados temporários
from .database import *


def get_user(user_id: int):
    if user_id < 0 or user_id > len(users_db):
        raise ValueError("User ID is out of range")

    if user_id not in users_db:
        raise ValueError("User not found")

    return users_db[user_id]
def get_evento(evento_id: int):
    if evento_id not in evento_db:
        raise ValueError("Evento not found")

    return evento_db[evento_id]
def get_tipo(tipo_id: int):

    if tipo_id not in tipo_db:
        raise ValueError("Tipo not found")

    return tipo_db[tipo_id]
def get_local(local_id: int):
    
    if local_id not in local_db:
        raise ValueError("Local not found")
    
    
    return local_db[local_id]
def get_evento_by_nome(evento_nome: str):
    for evento in evento_db.values():
        if evento["nome"] == evento_nome:
            return evento
    return None

def get_user_by_email(email: str):
    for user in users_db.values():
        if user["email"] == email:
            return user
    return None

def get_tipo_by_nome(tipo_nome: str):
    for tipo in tipo_db.values():
        if tipo["nome"] == tipo_nome:
            return tipo
    return None
def get_users(skip: int = 0, limit: int = 100):
    return list(users_db.values())[skip : skip + limit]

def get_eventos(skip: int = 0, limit: int = 100):
    return list(evento_db.values())[skip : skip + limit]
def get_tipos(skip: int = 0, limit: int = 100):
    return list(tipo_db.values())[skip : skip + limit]
def get_locais(skip: int = 0, limit: int = 100):
    return list(local_db.values())[skip : skip + limit]
def create_user(user: dict):
    global user_id_counter
    new_user = {
        "id": user_id_counter,
        "email": user["email"],
        "hashed_password": user["password"] + "notreallyhashed",
        "is_active": True,
        "items": [],
    }
    users_db[user_id_counter] = new_user
    user_id_counter += 1
    return new_user
def create_evento (evento: dict):
    global evento_id_counter
    new_evento = {
        "id": evento_id_counter,
        "nome": evento["nome"],
        "data": evento["data"],
        "hora": evento["hora"],
        "local_id": evento["local_id"],
        "tipo_id": evento["tipo_id"],
    }
    evento_db[evento_id_counter] = new_evento
    evento_id_counter += 1
    return new_evento
def create_tipo (tipo: dict):
    global tipo_id_counter
    new_tipo = {
        "id": tipo_id_counter,
        "nome": tipo["nome"],
        "descricao": tipo["descricao"],
        "publico_alvo": tipo["publico_alvo"],
        "evento_id": tipo["evento_id"]
    }
    tipo_db[tipo_id_counter] = new_tipo
    tipo_id_counter += 1
    return new_tipo
def create_local(local: dict):
    global local_id_counter
    new_local = {
        "id": local_id_counter,
        "nome": local["nome"],
        "endereco": local["endereco"],
        "capacidade": local["capacidade"],
        "evento_id": local["evento_id"]
    }
    local_db[local_id_counter] = new_local
    local_id_counter += 1
    return new_local

def get_items(skip: int = 0, limit: int = 100):
    return list(items_db.values())[skip : skip + limit]


def create_user_item(user_id: int, item: dict):

    global item_id_counter
    new_item = {
        "id": item_id_counter,
        "title": item["title"],
        "description": item.get("description", None),
        "owner_id": user_id,
    }
    items_db[item_id_counter] = new_item
    users_db[user_id]["items"].append(new_item)
    item_id_counter += 1
    return new_item
def get_local_by_nome(local_nome: str):
    for local in local_db.values():
        if local["nome"] == local_nome:
            return local
    return None
def update_local(local_id: int, local: dict):
    if local_id not in local_db:
        raise ValueError("local not found")
    
    for key, value in local.items(): 
        print(key, value)
        if key == "evento_id" and value != None:
            if value in local_db:  
                local_db[local_id]["local_id"] = value
            else:
                raise ValueError("Local not found")
        else:
            if value != None:
                local_db[local_id][key] = value
    return local_db[local_id]

def delete_local(local_id: int):
    if local_id not in local_db:
        raise ValueError("Local not found")
    
    del local_db[local_id]
    return {"message": "Local deleted successfully"}

# Funções CRUD para Evento

def update_evento(evento_id: int, evento: dict):
    if evento_id not in evento_db:
        raise ValueError("Evento not found")
    
    for key, value in evento.items(): 
        print(key, value)
        if key == "local_id" and value != None:
            if value in local_db:  
                evento_db[evento_id]["local_id"] = value
            else:
                raise ValueError("Local not found")
        
        # Atualiza o tipo_id se for válido
        elif key == "tipo_id" and value != None:
            if value in tipo_db:  # Verifica se o tipo existe no banco de dados
                evento_db[evento_id]["tipo_id"] = value
            else:
                raise ValueError("Tipo not found")
        
        # Atualiza qualquer outro campo do evento
        else:
            if value != None:
                evento_db[evento_id][key] = value

    return evento_db[evento_id]

def delete_evento(evento_id: int):
    if evento_id not in evento_db:
        raise ValueError("Evento not found")
    
    del evento_db[evento_id]
    return {"message": "Evento deleted successfully"}

# Funções CRUD para Tipo

def update_tipo(tipo_id: int, tipo: dict):
    if tipo_id not in tipo_db:
        raise ValueError("tipo not found")
    
    for key, value in tipo.items(): 
        print(key, value)
        if key == "evento_id" and value != None:
            if value in local_db:  
                tipo_db[tipo_id]["local_id"] = value
            else:
                raise ValueError("Local not found")
        else:
            if value != None:
                tipo_db[tipo_id][key] = value

    return tipo_db[tipo_id]

def delete_tipo(tipo_id: int):
    if tipo_id not in tipo_db:
        raise ValueError("Tipo not found")
    
    del tipo_db[tipo_id]
    return {"message": "Tipo deleted successfully"}