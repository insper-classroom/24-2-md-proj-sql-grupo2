from sqlalchemy import text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

Base = declarative_base()

# Obter informações de configuração do banco de dados a partir das variáveis de ambiente
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "meubanco")

# Conexão com o banco de dados
default_engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}")

# Criação do banco de dados se não existir
with default_engine.begin() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))

# Conecte-se ao banco de dados recém-criado
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criação das tabelas no novo banco de dados
with engine.begin() as conn:
    # Cria a tabela 'locais'
    conn.execute(
        text(
            """
        CREATE TABLE IF NOT EXISTS locais (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            endereco VARCHAR(255) NOT NULL,
            capacidade INT NOT NULL,
            telefone VARCHAR(20),
            temEstacionamento BOOLEAN NOT NULL DEFAULT FALSE,
            acessibilidade BOOLEAN NOT NULL DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        );
    """
        )
    )

    # Cria a tabela 'tipo_evento'
    conn.execute(
        text(
            """
        CREATE TABLE IF NOT EXISTS tipo (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            descricao VARCHAR(255) NOT NULL,
            publico_alvo VARCHAR(255) NOT NULL,
            objetivo VARCHAR(255) NOT NULL,
            ehPresencial BOOLEAN NOT NULL DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        );
    """
        )
    )

    # Cria a tabela 'eventos'
    conn.execute(
        text(
            """
    CREATE TABLE IF NOT EXISTS eventos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        descricao VARCHAR(255) NOT NULL,
        data DATE NOT NULL,
        ehFormal BOOLEAN NOT NULL DEFAULT FALSE,
        custoIngresso INT NOT NULL,
        contato VARCHAR(20) NOT NULL,
        horaInicio DATETIME  NOT NULL,
        horaFim DATETIME  NOT NULL,
        tipo_id INT NOT NULL,  -- Foreign key adicionada
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        CONSTRAINT fk_tipo_id FOREIGN KEY (tipo_id) REFERENCES tipo(id)  -- Definindo a foreign key
    );
"""
        )
    )

    # Cria a tabela de associação entre eventos e locais (many-to-many)
    conn.execute(
        text(
            """
        CREATE TABLE IF NOT EXISTS evento_local (
            evento_id INT,
            local_id INT,
            PRIMARY KEY (evento_id, local_id),
            FOREIGN KEY (evento_id) REFERENCES eventos(id) ON DELETE CASCADE,
            FOREIGN KEY (local_id) REFERENCES locais(id) ON DELETE CASCADE
        );
    """
        )
    )
