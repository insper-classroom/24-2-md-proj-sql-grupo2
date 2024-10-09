# dicionários para armazenar dados temporários
from .database import *

################################################################ READ ################################################################


# Retorna o evento de ID especificado:
def get_evento(evento_id: int):
    if evento_id not in evento_db:
        raise ValueError("Evento not found")

    return evento_db[evento_id]


# Retorna o tipo de evento pelo ID específico
def get_tipo(tipo_id: int):

    if tipo_id not in tipo_db:
        raise ValueError("Tipo not found")

    return tipo_db[tipo_id]


# Retorna o local do evento pelo ID específico
def get_local(local_id: int):

    if local_id not in local_db:
        raise ValueError("Local not found")

    return local_db[local_id]


# Retorna o evento de nome especificado, caso não exista nenhum evento com esse nome retorna "None"
def get_evento_by_nome(evento_nome: str):
    for evento in evento_db.values():
        if evento["nome"] == evento_nome:
            return evento
    return None


# Retorna o tipo de nome especificado, caso não exista nenhum tipo com esse nome retorna "None"
def get_tipo_by_nome(tipo_nome: str):
    for tipo in tipo_db.values():
        if tipo["nome"] == tipo_nome:
            return tipo
    return None


# Retorna o local de nome especificado, caso não exista nenhum local com esse nome retorna "None"
def get_local_by_nome(local_nome: str):
    for local in local_db.values():
        if local["nome"] == local_nome:
            return local
    return None


# Retorna todos os 100 primeiros eventos armazenados na tabela
def get_eventos(skip: int = 0, limit: int = 100):
    return list(evento_db.values())[skip : skip + limit]


# Retorna os 100 primeiros tipos armazenados na tabela
def get_tipos(skip: int = 0, limit: int = 100):
    return list(tipo_db.values())[skip : skip + limit]


# Retorna os 100 primeiros locais armazenados na tabela
def get_locais(skip: int = 0, limit: int = 100):
    return list(local_db.values())[skip : skip + limit]


########################################################################################################################################

################################################################ CREATE ################################################################


# Cria eventos e adiciona eles na tabela de eventos
def create_evento(evento: dict):
    global evento_id_counter
    new_evento = {
        "id": evento_id_counter,
        "nome": evento["nome"],
        "descricao": evento["descricao"],
        "data": evento["data"],
        "ehFormal": evento["ehFormal"],
        "custoIngresso": evento["custoIngresso"],
        "contato": evento["contato"],
        "horaInicio": evento["horaInicio"],
        "horaFim": evento["horaFim"],
        "local_id": evento["local_id"],
        "tipo_id": evento["tipo_id"],
    }
    evento_db[evento_id_counter] = new_evento
    evento_id_counter += 1
    return new_evento


# Cria tipos e adiciona eles na tabela de tipos
def create_tipo(tipo: dict):
    global tipo_id_counter
    new_tipo = {
        "id": tipo_id_counter,
        "nome": tipo["nome"],
        "descricao": tipo["descricao"],
        "publico_alvo": tipo["publico_alvo"],
        "objetivo": tipo["objetivo"],
        "ehPresencial": tipo["ehPrecencial"],
    }
    tipo_db[tipo_id_counter] = new_tipo
    tipo_id_counter += 1
    return new_tipo


# Cria locais e adiciona eles na tabela de locais
def create_local(local: dict):
    global local_id_counter
    new_local = {
        "id": local_id_counter,
        "nome": local["nome"],
        "endereco": local["endereco"],
        "capacidade": local["capacidade"],
        "telefone": local["telefone"],
        "temEstacionamento": local["temEstacionamento"],
        "acessibilidade": local["acessibilidade"],
        "event_id": local["event_id"],
    }
    local_db[local_id_counter] = new_local
    local_id_counter += 1
    return new_local


########################################################################################################################################

################################################################ UPDATE ################################################################


# Atualiza os dados de um evento que já exista na tabela
def update_evento(evento_id: int, evento: dict):
    if evento_id not in evento_db:
        raise ValueError("Evento not found")

    for key, value in evento.items():
        print(key, value)
        if key == "local_id" and value != None:
            evento_db[evento_id]["local_id"] = value

        # Atualiza o tipo_id se for válido
        elif key == "tipo_id" and value != None:
            evento_db[evento_id]["tipo_id"] = value

        # Atualiza qualquer outro campo do evento
        else:
            if value != None:
                evento_db[evento_id][key] = value

    return evento_db[evento_id]


# Atualiza os dados de um tipo que já existe na tabela
def update_tipo(tipo_id: int, tipo: dict):
    if tipo_id not in tipo_db:
        raise ValueError("tipo not found")

    for key, value in tipo.items():
        if value != None:
            tipo_db[tipo_id][key] = value

    return tipo_db[tipo_id]


# Atualiza os dados de um local já existente na tabela
def update_local(local_id: int, local: dict):
    if local_id not in local_db:
        raise ValueError("local not found")

    for key, value in local.items():
        if value != None:
            local_db[local_id][key] = value
    return local_db[local_id]


########################################################################################################################################

################################################################ DELETE ################################################################


# Deleta um evento já existente na tabela
def delete_evento(evento_id: int):
    if evento_id not in evento_db:
        raise ValueError("Evento not found")

    del evento_db[evento_id]
    return {"message": "Evento deleted successfully"}


# Deleta um tipo já existente na tabela
def delete_tipo(tipo_id: int):
    if tipo_id not in tipo_db:
        raise ValueError("Tipo not found")

    del tipo_db[tipo_id]
    return {"message": "Tipo deleted successfully"}


# Deleta um local já existente na tabela
def delete_local(local_id: int):
    if local_id not in local_db:
        raise ValueError("Local not found")

    del local_db[local_id]
    return {"message": "Local deleted successfully"}


########################################################################################################################################
