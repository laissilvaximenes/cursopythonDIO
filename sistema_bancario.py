# Depósito:
#   Depositar valores positivos na conta
#   Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato

# Saque:
#   O sistema deve permitir realizar 3 saques diários com limite máximo de R$500 por saque
#   Caso não tenha saldo, deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo
#   Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato

# Extrato:
#   Listar todos os depósitos e saques realizados na conta
#   No fim da listagem, deve conter o saldo atual da conta
#   Os valores devem ser exibidos utilizando o formato R$xxx.xx

# ------------------------------------------------------------------------------------------------------------------------

menu = """

Seja bem vindo(a)! Qual operação deseja realizar?

[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

==> """

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3
        

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Informe o valor a ser depositado:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido")
        

    elif opcao == 2:
        valor = float(input("Informe o valor do saque:"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES


        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite permitido.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == 3:
        print("\n ========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("\n ============================")
        
    elif opcao == 4:
        break
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!")