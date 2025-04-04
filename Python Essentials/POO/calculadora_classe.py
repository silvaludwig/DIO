class Calculadora:
    # def __init__(self, num1, num2):
    #     self.num1 = num1
    #     self.num2 = num2

    def soma(self, num1, num2):
        return num1 + num2
    
num1 = int(input())
num2 = int(input())

# Criando uma instância da calculadora
calc = Calculadora()

resultado = calc.soma(num1, num2)
print(resultado)