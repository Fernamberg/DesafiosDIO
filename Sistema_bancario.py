menu = """
*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *
▬▬▬▬▬▬▬▬▬▬▬▬ DIO INTERNATIONAL BANK ▬▬▬▬▬▬▬▬▬▬▬▬▬

============== LEGENDA DE OPÇÕES ================

[1] DEPÓSITO
[2] SAQUE
[3] EXTRATO
[x] SAIR
_________________________________________________

→ Digite aqui a opção escolhida: """ # menu do sistema bancário

saldo = 0 #valor disponível na conta
limite_valor_saque = 500 #valor máximo que pode ser sacado por vez
limite_quant_saques = 3 #quantidade máxima de saques diários
quant_saques = 0 #conta a quantidade de saques
extrato = "" # recebe movimentação da conta entre depósitos e saques

while True:
    
    opcao_escolhida = input(menu)
# DEPÓSITO
    if opcao_escolhida == "1":
        valor = float(input("_________________________________________________\nQual o valor? "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("_________________________________________________\nValor depositado com sucesso!")
            nova_operacao = input("Deseja realizar outra operação [S/N]? ")
            if nova_operacao == "S":
                continue
            else:
                print("Seção encerrada!")
                break
        else:
            print("Operação inválida!")

    elif opcao_escolhida == "2":
        valor = float(input("_________________________________________________\nQual o valor? "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_valor_saque
        excedeu_saques = quant_saques >= limite_quant_saques

        if excedeu_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print("O valor ultrapassa o limite por saque.")
        elif excedeu_saques:
            print("Limite de saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: - R$ {valor:.2f}\n"
            quant_saques += 1
            print("_________________________________________________\nSaque realizado!")
            nova_operacao = input("_________________________________________________\nDeseja realizar outra operação [S/N]? ")
            if nova_operacao == "S":
                continue
            else:
                print("Seção encerrada!")
                break

        else:
            print("Operação inválida!")
    
    elif opcao_escolhida == "3":
        print("\n_______________E X T R A T O_____________________")
        print("Transações inexistentes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("_________________________________________________")
    elif opcao_escolhida == "x":
        print("Seção encerrada!")
        break
    else:
        print("Operação inválida!")

