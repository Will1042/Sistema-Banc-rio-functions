import textwrap

def menu():

    menu = """\n
    ============Menu============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo Usuário
    [nc]\tNova Conta
    [lc]\tlistar contas
    [q]\tSair 
    ==> """
    return input(textwrap.dedent(menu))

opcao = input(menu)

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor}"
        print("Depósito realizado com sucesso!!!")
    else:
        print("Erro.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    
    if numero_saques < limite_saques:
        if valor > limite:
            print("Valor ultrapassa limite de saque estimulado em R$500.")
        elif valor > saldo:
            print(f"Não foi possível realizar a operação devido a falta de saldo. Saldo da conta atual é: R${saldo}")
        else:
            saldo -= valor
            numero_saques += 1
            extrato += f" Saque:\tR$ {valor}"
            print(f"Saque de R${valor} realizado com sucesso!")

    elif numero_saques > limite_saques:
        print("Você atingiu o limite de 3 saques diarios!!!")
    else:
        print("Operação falhou! O valor informado é inválido")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n==================Extrato==================")
    print("Não foram realizadas movimentações."if not extrato else extrato)
    print(f"\nSaldo:\tR$ {saldo}")
    print("===========================================")

def novo_usuario(usuarios):
    cpf = input("Insira o CPF do cliente(somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário cadastrado com este cpf!")
        return 
    
    nome = input("Insira o nome completo do cliente: ")
    data_nascimento = input("Insira a data de nascimento(01/01/1900): ")
    endereco = input("Insira o endereço(logradouro, nro - bairro - cidade/sigla estado): ")
        
    usuarios.append({
    'nome': nome,
    'data_nascimento': data_nascimento,
    'cpf': cpf,
    'endereco': endereco,
    })

    return usuarios

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Insira o cpf do usuario: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!!!")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuario não encontrado, criação de conta encerrado!!!")

def listar_usuarios(contas):
    print("================Usuarios================")
    print(contas)
    print("========================================")

def main():
    AGENCIA = "0001"

    saldo = 1000
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []

    while True:
        
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Insira o valor para deposito: "))
            
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Insira o valor para Saque: "))

            saldo, extrato = sacar(saldo=saldo,
                                    valor=valor,
                                    extrato=extrato,
                                    limite=limite,
                                    numero_saques=numero_saques,
                                    limite_saques=limite_saques)

        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)
            print(contas)
            
        elif opcao == "nu":
            novo_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_usuarios(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione a operação desejada novamente!")
        

main()