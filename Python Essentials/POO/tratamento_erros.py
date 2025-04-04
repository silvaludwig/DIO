from pathlib import Path

try: #tentar executar o código abaixo
    arquivo = open("meu-arquivo.txt") #tenta abrir um arquivo e o atribui a variavel 
except FileNotFoundError as exc: #caso levante esse erro, atribua a exc o seu valor 
    print(f"Arquivo não encontrado! Erro: {exc}") #exibe mensagem de exceção levantada e especifica o erro

ROOT_PATH = Path(__file__).parent #acessa o caminho da pasta atual e atribui a variavel ROOT_PATH

try: #tratanebti de exceção para o caso do arquivo a ser aberto ser um diretório e não um arquivo em si
    arquivo = open(ROOT_PATH / "novo-diretorio")
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arquivo. Erro: {exc}")