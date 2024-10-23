from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship
from .database import Base

# Tabela de associação entre eventos e locais
evento_local = Table(
    'evento_local',
    Base.metadata,
    Column('evento_id', Integer, ForeignKey('eventos.id', ondelete="CASCADE"), primary_key=True),
    Column('local_id', Integer, ForeignKey('locais.id', ondelete="CASCADE"), primary_key=True)
)

# Tabela de associação entre eventos e tipos de evento


class Tipo(Base):
    __tablename__ = "tipo"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False, index=True)
    descricao = Column(String(255), nullable=False)
    publico_alvo = Column(String(255), nullable=False)
    objetivo = Column(String(255), nullable=False)
    ehPresencial = Column(Boolean, nullable=False, default=True)
    
    # Relacionamento inverso
   


class Local(Base):
    __tablename__ = "locais"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False, index=True)
    endereco = Column(String(255), nullable=False)
    capacidade = Column(Integer, nullable=False)
    telefone = Column(String(20))
    temEstacionamento = Column(Boolean, nullable=False, default=False)
    acessibilidade = Column(Boolean, nullable=False, default=False)
    
    # Relacionamento inverso
    eventos = relationship("Evento", secondary=evento_local, back_populates="locais")


class Evento(Base):
    __tablename__ = "eventos"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False, index=True)
    descricao = Column(String(255), nullable=False)
    data = Column(DateTime, nullable=False, index=True)
    ehFormal = Column(Boolean, nullable=False, default=False)
    custoIngresso = Column(Integer, nullable=False)
    contato = Column(String(20), nullable=False)
    horaInicio = Column(DateTime, nullable=False)
    horaFim = Column(DateTime, nullable=False)
    tipo_id = Column(Integer, ForeignKey("tipo.id"))
    tipo = relationship("Tipo") 
    # Relacionamentos
    locais = relationship("Local", secondary=evento_local, back_populates="eventos")