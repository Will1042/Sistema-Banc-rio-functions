# Próximo objetivo Separar as funções de saque, depósito e extratoss em funções. Criar duas novas funções cadastrar usuário (cliente) e cadastrar conta bancária (corrente) vincular está conta com o usuario.

# 5 minutos o restante do desafio...

menu = { """[d] Depositar / [s] sacar / [e] extrato / [q] Sair => """}

saldo = 1000
limite_saque_diario = 500
extrato_saques = []
extrato_depositos = []
numero_saques = 0
limite_saque_diario = 3
saques_feitos = 0

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("deposito")
        
        deposito = int(input("Insira o valor para deposito: "))
        
        if deposito > 0:
            saldo += deposito
            
            deposito_extrato = str(deposito)
            extrato_depositos.append("R$" + deposito_extrato)
        
        else:
            print("Operação inválida, favor inserir valores maior que 0")
    elif opcao == "s":
        
        saque = int(input("Insira o valor desejado para saque: "))
        saque_extrato = str(saque)
        
        if saques_feitos < limite_saque_diario:
            if saque > 500:
                print("Valor ultrapassa limite de saque estipulado em R$500!")
            elif saque > saldo:
                print(f"Não foi possível realizar a operação devido a falta de saldo. Saldo da conta atual é: R${saldo}")
            else:
                saldo -= saque
                saques_feitos += 1

                extrato_saques.append("R$" + saque_extrato)
        else: 
            print("Você atingiu o limite de 3 saques diarios!!!")
        
    elif opcao == "e":
        print(f"Saques realizados: {extrato_saques}")
        print(f"Depositos realizados: {extrato_depositos}")
        print(f"Seu saldo atual é: R${saldo}")
    
    elif opcao == "q":
        print("sair")
        break
    else:
        print("Operação inválida, por favor selecione a operação desejada novamente!")
    