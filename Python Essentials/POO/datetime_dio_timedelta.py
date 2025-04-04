from datetime import datetime, timedelta

tipo_de_carro = input("Tamanho do carro P, M, G: ").upper()

tempo_pequeno = 30 #variação de tempo (timedelta)
tempo_medio = 45
tempo_grande = 60

data_atual = datetime.now() # pega a data atual de acordo com o sistema

if tipo_de_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou {data_atual} e ficará pronto às {data_estimada}")

elif tipo_de_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou {data_atual} e ficará pronto às {data_estimada}")

elif tipo_de_carro == 'G':
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou {data_atual} e ficará pronto às {data_estimada}")

else:
    print("Opção inválida")