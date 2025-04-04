class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando Motor")

class Carro(Veiculo):
    pass

class Motocicleta(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("preta", "abc-3456", 2)
moto.ligar_motor()

carro = Carro("azul", "jht-6789", 4)
carro.ligar_motor()

caminhao = Caminhao("amarelo", "huj-0987", 8, False)
caminhao2 = Caminhao("Verde", "huj-0987", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
caminhao2.esta_carregado()