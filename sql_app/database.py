from sqlalchemy import text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME =  "meubanco4"
Base = declarative_base()
# Conexão com o banco de dados padrão (para PostgreSQL use "postgresql://")
default_engine = create_engine("mysql+pymysql://{DB_HOST}:{DB_USER}!@{DB_PASSWORD}")
# Nome do banco de dados que você quer criar
database_name = "meubanco"

# Criação do banco de dados se não existir
with default_engine.begin() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {database_name}"))

# Conecte-se ao banco de dados recém-criado
engine = create_engine(f"mysql+pymysql://{DB_HOST}:{DB_USER}!@{DB_PASSWORD}/{database_name}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Criação das tabelas no novo banco de dados
with engine.begin() as conn:
    # Cria a tabela 'locais'
    conn.execute(text("""
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
    """))

    # Cria a tabela 'tipo_evento'
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS tipo_evento (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            descricao VARCHAR(255) NOT NULL,
            publico_alvo VARCHAR(255) NOT NULL,
            objetivo VARCHAR(255) NOT NULL,
            ehPresencial BOOLEAN NOT NULL DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        );
    """))

    # Cria a tabela 'eventos'
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS eventos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            descricao VARCHAR(255) NOT NULL,
            data DATE NOT NULL,
            ehFormal BOOLEAN NOT NULL DEFAULT FALSE,
            custoIngresso INT NOT NULL,
            contato VARCHAR(20) NOT NULL,
            horaInicio TIME NOT NULL,
            horaFim TIME NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        );
    """))

    # Cria a tabela de associação entre eventos e locais (many-to-many)
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS evento_local (
            evento_id INT,
            local_id INT,
            PRIMARY KEY (evento_id, local_id),
            FOREIGN KEY (evento_id) REFERENCES eventos(id) ON DELETE CASCADE,
            FOREIGN KEY (local_id) REFERENCES locais(id) ON DELETE CASCADE
        );
    """))

    # Cria a tabela de associação entre eventos e tipos de evento (many-to-many)
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS evento_tipo (
            evento_id INT,
            tipo_id INT,
            PRIMARY KEY (evento_id, tipo_id),
            FOREIGN KEY (evento_id) REFERENCES eventos(id) ON DELETE CASCADE,
            FOREIGN KEY (tipo_id) REFERENCES tipo_evento(id) ON DELETE CASCADE
        );
    """))