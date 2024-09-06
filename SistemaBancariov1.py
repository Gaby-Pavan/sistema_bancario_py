menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Digite o valor do depósito"))
        if valor > 0:
            saldo += valor
            extrato += (f"Depósito: R$ {valor:.2f}\n")
        else: 
            print("Falha na operação. Informe um valor válido")
    elif opcao == "s":
        saque = float(input("Digite o valor desejado para o saque"))
        if saque > saldo:
            print ('Operação Falhou. Saldo insuficiente')
        elif saque > limite:
            print ('Operação falhou. Valor do saque superior ao limite')
        elif numero_saques >= limite_saques:
            print ('Falhou. Número limite de saques diários excedido')
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
        else:
            print("Falha na operação. Valor informado é inválido")
    elif opcao == "e":
        print("\n********** EXTRATO **********")
        print("Sem movimentações no extrato" if not extrato else extrato)
        print(f"\nSaldo Final: {saldo:.2f}")
        print("*******************************")

    elif opcao == "q":
        break
    else:
        print('Operação inválida, por favor selecione novamente')
