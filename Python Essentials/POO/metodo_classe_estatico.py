class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade 

    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(idade, nome)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))