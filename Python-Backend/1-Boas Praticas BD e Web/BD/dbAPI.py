import sqlite3
from pathlib import Path

#criando uma variável ROOT_PATH pra que o BD esteja na pasta atual do projeto
ROOT_PATH = Path(__file__).parent

#Estabelecendo conexão com o BD. Caso ele não exista, está criando um novo
conexao = sqlite3.connect(ROOT_PATH / "teste_db.db")

#cria uma instancia de cursor(), que é a base pra comandos sql dentro do python
cursor = conexao.cursor()

#criando uma tabela no banco de dados
def criar_tabela(conexao, cursor):
    #utilizando a instancia criada anteriormente, cria uma tabela clientes, caso não exista no BD
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS clientes (clientes_ID INTEGER PRIMARY KEY AUTOINCREMENT, "
        "clientes_NOME VARCHAR(100), clientes_EMAIL VARCHAR(150));"
        )
    conexao.commit()

#inserindo valores na tabela criada anteriormente
def inserir_registros(conexao, cursor, clientes_NOME, clientes_EMAIL):
    #criando uma variavel data que armazena os dados que eu quero inserir na tabela
    data = (clientes_NOME, clientes_EMAIL)

    #chama a função execute na instancia cursor com os comandos SQL pra inserir os dados
    cursor.execute("INSERT INTO clientes(clientes_NOME, clientes_EMAIL) VALUES (?,?);", data)

    #chama a função commit da instancia conexao, o que faz com que os dados sejam persistidos na tabela
    conexao.commit()

#atualizar registros na tabela clientes
def atualizar_registros(conexao, cursor, clientes_NOME, clientes_EMAIL, clientes_ID):
    data = (clientes_NOME, clientes_EMAIL, clientes_ID)
    cursor.execute("UPDATE clientes SET clientes_NOME=?, clientes_EMAIL=? WHERE clientes_ID=?;", data)
    conexao.commit()

#excluir registros na tabela clientes
def excluir_registros(conexao, cursor, clientes_ID):
    data = (clientes_ID,)
    cursor.execute("DELETE FROM clientes WHERE clientes_ID=?;", data)
    conexao.commit()

#inserir em lote
def inserir_muitos(conexao, cursor, dados):
    #metodo executemany() pra inserir dados em lote no db
    cursor.executemany("INSERT INTO clientes (clientes_NOME, clientes_EMAIL) VALUES (?,?)", dados)
    conexao.commit()

#consultar um cliente por vez
def recuperar_clientes(cursor, clientes_ID):
    cursor.execute("SELECT * FROM clientes WHERE clientes_ID=?;", (clientes_ID,))
    return cursor.fetchone()

#listar todos os clientes
def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY clientes_NOME;")


dados = [
    ("Guilherme", "gui@email.com"),
    ("Giovana", "giov@email.com"),
    ("Joãozin", "liljohn@email.com"),
    ("Pedro", "pedro@email.com"),
    ("Fernanda", "nanda@email.com")
]
# inserir_registros(conexao, cursor, "Geraldo", "geraldo@email.com")
# atualizar_registros(conexao, cursor, "Jeronimo", "jeronimo@email.com", 1)
# excluir_registros(conexao, cursor, 1)
# inserir_muitos(conexao, cursor, dados)
cliente = recuperar_clientes(cursor, 3)
print(cliente)
for info in cliente:
    print(info)
print("============================")
clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)
print("============================")

#tratamento de erro na hora da operação em SQL no db
try:
    cursor.execute("INSERT INTO clientes (clientes_NOME, clientes_EMAIL) VALUES (?,?)", ("Teste1", "teste1@email.com"))
    cursor.execute("INSERT INTO clientes (clientes_ID, clientes_NOME, clientes_EMAIL) VALUES (?,?,?)", (2, "Teste2", "teste2@email.com"))
    conexao.commit()
except Exception as Exc:
    print(f"Ops, algo deu errado: {Exc}")
    conexao.rollback() #rollback é uma função que desfaz o último commit, no caso se der algum erro na operação