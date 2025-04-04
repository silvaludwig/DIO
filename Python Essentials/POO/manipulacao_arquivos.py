import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent #define a pasta atual onde o arquivo do programa está, sem contar o próprio arquivo

os.mkdir(ROOT_PATH / "novo-diretorio") #cria uma nova pasta no path chamada novo-diretorio

arquivo = open(ROOT_PATH / "novo.txt", "w") #cria e abre um novo arquivo .txt na pasta com a função de escrita
arquivo.close() #fecha o arquivo criado e aberto anteriormente

os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt") #renomea o arquivo de novo pra alterado. o primeiro argumento é o arquivo antes da alteração, o segundo é o novo nome do arquivo

os.remove(ROOT_PATH / "alterado.txt") #apaga o arquivo selecionado do path, no caso o arquivo recem alterado

shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt") #move o arquivo da pasta atual pra pasta novo-diretorio. Mema coisa ali em cima, o primeiro argumento é onde o arquivo está atualmente, o segundo é o destino final do arquivo.