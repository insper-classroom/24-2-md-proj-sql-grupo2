# Dicionários pré-setados para teste

local_db = {
    1: {
        "id": 1,
        "nome": "Auditório Principal",
        "endereco": "Av. Paulista, 1000",
        "capacidade": 300,
        "evento_id": [1],
    },
    2: {
        "id": 2,
        "nome": "Sala de Conferência 1",
        "endereco": "Rua Augusta, 500",
        "capacidade": 50,
        "evento_id": [2],
    },
}

tipo_db = {
    1: {
        "id": 1,
        "nome": "Palestra",
        "descricao": "Evento focado em discussões e apresentações",
        "publico_alvo": "Estudantes e profissionais",
        "evento_id": [1],
    },
    2: {
        "id": 2,
        "nome": "Workshop",
        "descricao": "Treinamento prático com interação",
        "publico_alvo": "Público geral",
        "evento_id": [2],
    },
}

evento_db = {
    1: {
        "id": 1,
        "nome": "Tech Talk 2024",
        "data": "2024-11-15",
        "local_id": [1],
        "tipo_id": [1],
    },
    2: {
        "id": 2,
        "nome": "Workshop de Programação",
        "data": "2024-12-01",
        "local_id": [2],
        "tipo_id": [2],
    },
}

local_id_counter = 3
tipo_id_counter = 3
evento_id_counter = 3
