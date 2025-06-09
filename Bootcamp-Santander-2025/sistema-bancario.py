class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.limite_saque = 500
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite_saque
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def ver_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("=========================================")


def main():
    conta = ContaBancaria()

    while True:
        print("\n=============== MENU ===============")
        print("[d] Depositar")
        print("[s] Sacar")
        print("[e] Extrato")
        print("[q] Sair")
        print("===================================")

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
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()