from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:30"
mascara_ptbr = "%d/%m/%y"

print(data_hora_atual.strftime(mascara_ptbr)) #imprime a data atualcom a máscara/formato predefinido