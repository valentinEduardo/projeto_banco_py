opcao = -1
numero_saque = 3
saques_realizados = []
saldo = 1000
i=0
while opcao !=0:
    opcao = int(input("1- Sacar\n2- Depositar\n3- Extrato\n0- Sair\n"))
    if opcao==1:
        saque = float(input("Quanto deseja sacar?"))

        if saque<0 or saque>saldo:
            print("Valor digitado inválido")
        elif saque<=saldo and saque<=500 and numero_saque>0 and saldo>0:
            saldo-=saque
            numero_saque-=1
            saques_realizados.insert(i, saque)
            i+=1
            print(saques_realizados)
            print(f"Saque realizado com sucesso! Seu saldo agora é R${saldo}")
        elif saldo == 0:
            print("Seu saldo está zerado")
        else:
            print("Quantidade de saque diario excedida ou valor inválido")
    elif opcao==2:
        deposito = float(input("Digite o valor que deseja depositar"))

        if deposito<0:
            print("Valor de deposito inválido")
        else:
            saldo+=deposito
            print(f"Deposito realizado com sucesso! Seu saldo agora é de R${saldo}")
    else:
        print("Este é o seu extrato")
        for numeros in saques_realizados:
            print(f"-R${numeros}")

