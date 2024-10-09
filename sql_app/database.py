# Dicionários pré-setados para teste

local_db = {
    1: {
        "id": 1,
        "nome": "Centro de Convenções",
        "endereco": "Av. das Nações, 1234",
        "capacidade": 500,
        "telefone": "(11) 1234-5678",
        "temEstacionamento": 1,
        "acessibilidade": 1,
        "event_id": [1],
    },
    2: {
        "id": 2,
        "nome": "Espaço de Eventos do Campus",
        "endereco": "Rua Universitária, 789",
        "capacidade": 200,
        "telefone": "(11) 8765-4321",
        "temEstacionamento": 0,
        "acessibilidade": 1,
        "event_id": [2],
    },
}


tipo_db = {
    1: {
        "id": 1,
        "nome": "Palestra",
        "descricao": "Evento de caráter informativo com apresentação de palestrantes",
        "publico_alvo": "Profissionais de tecnologia",
        "objetivo": "Disseminar conhecimento tecnológico",
        "ehPresencial": 1,
    },
    2: {
        "id": 2,
        "nome": "Oficina",
        "descricao": "Treinamento prático com participação ativa",
        "publico_alvo": "Desenvolvedores iniciantes",
        "objetivo": "Ensinar boas práticas de desenvolvimento",
        "ehPresencial": 1,
    },
}


evento_db = {
    1: {
        "id": 1,
        "nome": "Tech Talk 2024",
        "descricao": "Discussões sobre tendências tecnológicas",
        "data": "2024-11-15",
        "ehFormal": 0,
        "custoIngresso": 100,
        "contato": "techtalk@eventos.com",
        "horaInicio": "10:00",
        "horaFim": "12:00",
        "local_id": [1],
        "tipo_id": [1],
    },
    2: {
        "id": 2,
        "nome": "Workshop de Programação",
        "descricao": "Oficina prática de programação",
        "data": "2024-12-01",
        "ehFormal": 0,
        "custoIngresso": 50,
        "contato": "workshop@eventos.com",
        "horaInicio": "14:00",
        "horaFim": "17:00",
        "local_id": [2],
        "tipo_id": [2],
    },
}


local_id_counter = 3
tipo_id_counter = 3
evento_id_counter = 3
