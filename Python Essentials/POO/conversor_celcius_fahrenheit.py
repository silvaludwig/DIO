#TODO: Crie uma classe para converter temperaturas de Celsius para Fahrenheit e um método que realiza o cálculo de conversão:
class ConversorTemperatura:
  
  def  celsius_para_fahrenheit(self, grau):
    self.grau = grau
    # fahrenheit=(celsius*9/5)+32
    return (grau*9/5)+32
    
# Entrada do usuário
celsius = float(input())

# TODO: Crie uma instância do conversor:
conversor = ConversorTemperatura()


fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)