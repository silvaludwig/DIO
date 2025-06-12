from colorama import Fore, Style
import random

class Usuario:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

class ContaBancaria:
    def __init__(self, usuario):
        self.usuario = usuario
        self.agencia = "0001"
        self.numero_conta = self.gerar_numero_conta()
        self.saldo = 0
        self.extrato = []
        self.limite_saque = 500
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    @staticmethod
    def gerar_numero_conta():
        return str(random.randint(10000, 99999))

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"{Fore.GREEN}Depósito de R$ {valor:.2f} realizado com sucesso!{Style.RESET_ALL}")
            return True
        print(f"{Fore.RED}Operação falhou! O valor informado é inválido.{Style.RESET_ALL}")
        return False

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite_saque
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print(f"{Fore.RED}Operação falhou! Você não tem saldo suficiente.{Style.RESET_ALL}")
        elif excedeu_limite:
            print(f"{Fore.RED}Operação falhou! O valor do saque excede o limite.{Style.RESET_ALL}")
        elif excedeu_saques:
            print(f"{Fore.RED}Operação falhou! Número máximo de saques excedido.{Style.RESET_ALL}")
        elif valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            print(f"{Fore.GREEN}Saque de R$ {valor:.2f} realizado com sucesso!{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Operação falhou! O valor informado é inválido.{Style.RESET_ALL}")
        return False

    def ver_extrato(self):
        print(f"\n{Fore.BLUE}================ EXTRATO ================{Style.RESET_ALL}")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in self.extrato:
                if "Depósito" in movimento:
                    print(f"{Fore.GREEN}{movimento}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}{movimento}{Style.RESET_ALL}")
        print(f"\nSaldo atual: {Fore.YELLOW}R$ {self.saldo:.2f}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}========================================={Style.RESET_ALL}")


class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, usuario):
        conta = ContaBancaria(usuario)
        self.contas[conta.numero_conta] = conta
        return conta

    def autenticar(self, numero_conta):
        return self.contas.get(numero_conta)


def criar_usuario():
    print(f"\n{Fore.CYAN}===== CRIAR USUÁRIO ====="{Style.RESET_ALL})
    nome = input("Nome completo: ")
    cpf = input("CPF (somente números): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ")
    return Usuario(nome, cpf, endereco)


def criar_conta_corrente(banco, usuario):
    conta = banco.criar_conta(usuario)
    print(f"\n{Fore.GREEN}=== CONTA CRIADA COM SUCESSO! ==="{Style.RESET_ALL}")
    print(f"Agência: {conta.agencia}")
    print(f"C/C: {conta.numero_conta}")
    print(f"Titular: {usuario.nome}")
    return conta


def menu_conta(conta):
    while True:
        print(f"\n{Fore.CYAN}=============== MENU ==============="{Style.RESET_ALL})
        print("[d] Depositar")
        print("[s] Sacar")
        print("[e] Extrato")
        print("[q] Sair")
        print(f"{Fore.CYAN}==================================="{Style.RESET_ALL})

        opcao = input("=> ").lower()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            conta.sacar(valor)
        elif opcao == "e":
            conta.ver_extrato()
        elif opcao == "q":
            break
        else:
            print(f"{Fore.RED}Operação inválida, por favor selecione novamente a operação desejada.{Style.RESET_ALL}")


def main():
    banco = Banco()

    while True:
        print(f"\n{Fore.YELLOW}========== SISTEMA BANCÁRIO =========="{Style.RESET_ALL}")
        print("[1] Criar usuário")
        print("[2] Criar conta corrente")
        print("[3] Acessar conta")
        print("[4] Sair")
        print(f"{Fore.YELLOW}====================================="{Style.RESET_ALL}")

        opcao = input("=> ")

        if opcao == "1":
            usuario = criar_usuario()
        elif opcao == "2":
            if 'usuario' not in locals():
                print(f"{Fore.RED}Você precisa criar um usuário primeiro!{Style.RESET_ALL}")
                continue
            conta = criar_conta_corrente(banco, usuario)
        elif opcao == "3":
            numero_conta = input("Informe o número da conta: ")
            conta = banco.autenticar(numero_conta)
            if conta:
                menu_conta(conta)
            else:
                print(f"{Fore.RED}Conta não encontrada!{Style.RESET_ALL}")
        elif opcao == "4":
            break
        else:
            print(f"{Fore.RED}Opção inválida!{Style.RESET_ALL}")


if __name__ == "__main__":
    import colorama
    colorama.init()
    main()