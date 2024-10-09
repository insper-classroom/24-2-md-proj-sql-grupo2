# Dicionários pré-setados para teste dos dados de locais, tipos e eventos

########## Locais ##########
# Dicionário que simula um banco de dados de locais, com detalhes como nome, endereço, capacidade e acessibilidade
local_db = {
    1: {
        "id": 1,
        "nome": "Centro de Convenções",
        "endereco": "Av. das Nações, 1234",
        "capacidade": 500,
        "telefone": "(11) 1234-5678",
        "temEstacionamento": 1,  # 1 significa que tem estacionamento
        "acessibilidade": 1,  # 1 significa que é acessível
        "event_id": [1],  # Lista de eventos associados ao local
    },
    2: {
        "id": 2,
        "nome": "Espaço de Eventos do Campus",
        "endereco": "Rua Universitária, 789",
        "capacidade": 200,
        "telefone": "(11) 8765-4321",
        "temEstacionamento": 0,  # 0 significa que não tem estacionamento
        "acessibilidade": 1,  # 1 significa que é acessível
        "event_id": [2],  # Lista de eventos associados ao local
    },
}

########## Tipos ##########
# Dicionário que simula um banco de dados de tipos de eventos, como palestras e oficinas
tipo_db = {
    1: {
        "id": 1,
        "nome": "Palestra",
        "descricao": "Evento de caráter informativo com apresentação de palestrantes",
        "publico_alvo": "Profissionais de tecnologia",  # Público alvo da palestra
        "objetivo": "Disseminar conhecimento tecnológico",  # Objetivo da palestra
        "ehPresencial": 1,  # 1 significa que é um evento presencial
    },
    2: {
        "id": 2,
        "nome": "Oficina",
        "descricao": "Treinamento prático com participação ativa",
        "publico_alvo": "Desenvolvedores iniciantes",  # Público alvo da oficina
        "objetivo": "Ensinar boas práticas de desenvolvimento",  # Objetivo da oficina
        "ehPresencial": 1,  # 1 significa que é um evento presencial
    },
}

########## Eventos ##########
# Dicionário que simula um banco de dados de eventos, incluindo detalhes como data, horários e locais
evento_db = {
    1: {
        "id": 1,
        "nome": "Tech Talk 2024",
        "descricao": "Discussões sobre tendências tecnológicas",
        "data": "2024-11-15",  # Data do evento
        "ehFormal": 0,  # 0 significa que o evento não é formal
        "custoIngresso": 100,  # Preço médio do ingresso
        "contato": "techtalk@eventos.com",  # Contato de email do evento
        "horaInicio": "10:00",  # Horário de início do evento
        "horaFim": "12:00",  # Horário de término do evento
        "local_id": [1],  # Locais associados ao evento (pode ter mais de um local)
        "tipo_id": 1,  # ID do tipo de evento, neste caso uma palestra
    },
    2: {
        "id": 2,
        "nome": "Workshop de Programação",
        "descricao": "Oficina prática de programação",
        "data": "2024-12-01",  # Data do evento
        "ehFormal": 0,  # 0 significa que o evento não é formal
        "custoIngresso": 50,  # Preço médio do ingresso
        "contato": "workshop@eventos.com",  # Contato de email do evento
        "horaInicio": "14:00",  # Horário de início do evento
        "horaFim": "17:00",  # Horário de término do evento
        "local_id": [2],  # Locais associados ao evento (pode ter mais de um local)
        "tipo_id": 2,  # ID do tipo de evento, neste caso uma oficina
    },
}

########## Contadores ##########
# Contadores para simular auto incremento de IDs de locais, tipos e eventos
# Quando um novo local, tipo ou evento é criado, o ID será gerado com base nesses contadores

local_id_counter = 3  # Contador de IDs de locais, começando do 3
tipo_id_counter = 3  # Contador de IDs de tipos, começando do 3
evento_id_counter = 3  # Contador de IDs de eventos, começando do 3
