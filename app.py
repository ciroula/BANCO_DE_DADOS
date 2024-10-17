"""
Banco de dados - Aprender linguagens que te deixem modelar o banco
	- SQL (Linguagem de consulta Estruturada)
	- Caracteristicas:
		-SELECT * FROM (Nome da tabela) ; (ponto e virgula necessário para informar que acabou o comando.
		- Irá consultar o BD na tabela (senha da tabela)
		
		- SGDB:
			- Gerenciar permissões de acesso (quem pode fazer e o que pode fazer).
			- ADMINISTRADOR DE BANCO DE DADOS (DBA)
			- CRIAR CONSULTAS PERSONALIZADAS
			- SELECT * FROM CLIENTES;
	-ORM: MAPEAMENTO OBJETO RELACIONAL
        - USAR A LINGUAGEM DE PROGRAMAÇÃO PARA MANIPULAR O BANCO DE DADOS.
    - INSTALANDO ORM PARA PYTHON:
		-pip install sqlalchemy


"""

import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#Criando banco de dados.
MEU_BANCO = create_engine("sqlite:///meubanco.db")

#Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando tabela.

Base = declarative_base()
class Cliente(Base): # nome de classe no singular
    __tablename__ = "clientes" # definir
    
        
	#Definindo campos da tabela
    """autoincrement = 
    	id - nome
        
        1- "Silvestre"
        2- "Fereira"
        
        salvar (1, "Silvestre")
        salvar ("Ferreira")
        
        o autoincrement ele automatiza o processo e tabela td
        
        """
    id = Column("id", Integer, primary_key= True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
	#Definindo atributos da classe.
    def __init__(self, nome:str, email:str, senha:str):
        self.nome = nome
        self.email = email
        self.senha = senha
#Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

#CRUD.
#Creat - Insert - Salvar.

#Limpando terminal
os.system("cls || clear")

def pedindo_informacoes_para_o_usuario():
    print("Solicitando dados para o usuário.")
    inserir_nome = input("Digite seu nome: ")
    inserir_email = input("Digite seu e-mail: ")
    inserir_senha = input("Digite sua senha: ")

    cliente = Cliente(nome = inserir_nome, email = inserir_email, senha = inserir_senha)
    session.add(cliente)
    session.commit()


def exibindo_dados_usuario():
    print("\nExibindo dados de todos os clientes.")
    lista_clientes = session.query(Cliente).all() #Consulta ao banco de dados "query" esconde o select - e vc seleciona a tabela que vc deseja que ele puxe

    for cliente in lista_clientes:
        print (f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha} ")

#Funcao para atualizar o cadastro, sobrepondo os dados
def atualizar_cadastro(cliente):
    nome_novo = input("Digite o novo nome: ")
    email_novo = input("Digite o email novo: ")
    senha_nova = input("Digite a senha nova: ")
    if nome_novo:

        cliente.nome = nome_novo
    if email_novo:
        cliente.email = email_novo
    if senha_nova:
        cliente.senha = senha_nova

    session.commit()



#Read - Select - Consulta
pedindo_informacoes_para_o_usuario()
exibindo_dados_usuario()


# U - Update - UPDATE - Atualizar
os.system("cls || clear")
escolha_atualizacao_cadastro = str(input("Deseja atualizar email do Cliente? "))
if escolha_atualizacao_cadastro == "sim".lower(): 
    email_cliente = input("Digite o email do cliente que será atualizado: ")

    cliente = session.query(Cliente).filter_by(email=email_cliente).first()

    if cliente:
        atualizar_cadastro(cliente)
    else:
        print("Cliente não encontrado.")
else:
    pass
# R - Read  - SELECT - Consulta

print("\nExibindo dados de todos os clientes.")
exibindo_dados_usuario()


# D - Delete - DELETE - Excluir
os.system("cls || clear")
escolha = str(input("Deseja excluir um cliente? Sim ou Nao: "))
if escolha == "sim".lower() :

    print("\nExcluindo os dados de um cliente.")
    email_cliente = input("Digite o e-mail do cliente que será excluído: ")

    cliente = session.query(Cliente).filter_by(email = email_cliente).first()

    if cliente:
        session.delete(cliente)
        session.commit()
        print(f"Cliente {cliente.nome} excluído com sucesso!")

    else:
        print("Cliente não encontrado.")
else:
    pass


#R - Read - SELECT - Consulta

print("\nExibindo dados de todos os clientes.")
lista_clientes = session.query(Cliente).all() #Consulta ao banco de dados "query" esconde o select - e vc seleciona a tabela que vc deseja que ele puxe

for cliente in lista_clientes:
    exibindo_dados_usuario

os.system("cls || clear")
consulta_cadastro_cliente = str(input("Deseja realizar consulta? "))
# R - Read - SELECT - Consulta
if consulta_cadastro_cliente == "sim".lower():

    print("Consultando os dados de apenas um cliente.")
    email_cliente = input("Digite o e-mail do cliente: ")

    cliente = session.query(Cliente).filter_by(email = email_cliente).first()

    if cliente:
        exibindo_dados_usuario()

    else:
        print("Cliente não encontrado.")
else:
    pass

#Fechando conexão
os.system("cls || clear")
exibindo_dados_usuario()


session.close()