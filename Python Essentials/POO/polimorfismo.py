class Passaro:
    def voar(self):
        print("VOANDO")

class Pardal(Passaro):
    def voar(self):
        super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("avestruz não voa")

def plano_de_voo(obj):
    obj.voar()

# na aula o professor criou essa classe avião, mas sendo filha de Passaro. 
# eu quis testar se funcionaria sem ser filha de Passaro, pq não fez muito sentido nesse exemplo
# usar uma classe nada a ver herdando de uma outra tbm nada a ver, sendo que eu poderia criar um 
# método dentro da própria classe pra executar a função que eu queria, que no caso é voar. 

class Avião:
    def voar(self):
        print("avião está voando")

plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Avião())
