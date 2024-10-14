"""
    BANCO DE DADOS
    - SQL (LINGUAGEM DE CONSULTAS ESTRUTURADAS)
    - EXEMPLO:
        - SELECT * FROM CLIENTES;
        - IRA CONSULTAR O BANCO DE DADOS NA TABELA CLIENTES.

        SGDB:
            - GERENCIAR PERMISSOES DE ACESSO
            - ADMINISTRADOR DE BANCO DE DADOS (BDA)
            - CRIAR CONSULTAS PERSONALIZADAS 
            - SELECT * FROM CLIENTES;
    - ORM: MAPEAMENTO OBJETO RELACIONAL
        - USAR A LIGUAGEM DE PROGRAMACAO PARA
          MANIPULAR O BANCO DE DADOS.
    - INSTALANDO ORM PARA PYTHON:
        - pip install sqlalchemy
"""

import os 
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

#criando conexao com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# criando tabela.
Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    #definindo campos da tabela
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome",String)
    email = Column("email",String)
    senha = Column("senha",String)

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

#criando atributos de classe
Base.metadata.create_all(bind=MEU_BANCO)

#CRUD
#Create - Insert - Salvar
os.system("cls || clear")
print("soicitando dados para o usuario")
inserir_nome = input("Digite o seu nome: ")
inserir_email = input("Digite o seu email: ")
inserir_senha = input("Digite a sua senha: ")

cliente = Cliente(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(cliente)
session.commit()

#Read - SELECT - Consultas
print("\nExibindo dados de todos os clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")
    
#U - Update - UPDATE - Atualizar
print("\nAtualizando dados do usuario.")
email_cliente = input("Digite o e-mail do cliente que sera atualizado: ")

cliente = session.query(Cliente).filter_by(email = email_cliente).first()

if cliente:
    cliente.nome = input("Digite seu nome: ")
    cliente.email = input("Digite seu e-mail: ")
    cliente.senha = input("Digite seu senha: ")

    session.commit()
else:
    print("Cliente nao encontrado.")

#Read - SELECT - Consultas
print("\nExibindo dados de todos os clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")