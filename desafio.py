#em virtude do que foi pedido para este desafio, tive que reescrever a lógica do código anterior
#ou seja, menos experimentos

LIMITE_SAQUES = 3
SAQUE_MAXIMO = 500

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[nu] Novo usuário
[lc] Listar contas
[q] Sair

=>\t"""

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("Operação inválida! O valor informado precisa ser maior que R$ 0,00.")
    else:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato

def sacar(*, saldo, valor, extrato, numero_saques):
    global LIMITE_SAQUES
    global SAQUE_MAXIMO
    
    if saldo < valor:
        print("Operação inválida! Saldo insuficiente.")
    elif valor > SAQUE_MAXIMO:
        print("Operação inválida! Valor máximo para saque é de R$500,00.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação inválida! Limite de saques diários atingido.")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        
    else:
        print("Operação inválida! O valor informado precisa ser maior que R$ 0,00.")
    return saldo, extrato, numero_saques
    
    
def emitir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=============================")
    
def criar_usuario(usuarios):
    cpf = ""
    while True:
        cpf = input("Informe o CPF aqui (números apenas):\t")
        if not cpf.isdigit():
            print("CPF inválido! Certifique-se de apenas escrever números.")
        else:
            break
            
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Este CPF já foi cadastrado anteriormente. Operação cancelada.")
            return
            
    nome = input("Informe o nome completo:\t")
    data_nascimento = input("Informe a data de nascimento (formato: dd-mm-aaaa):\t")
    endereco = input("Informe o endereço (formato: logradouro, nro - bairro - cidade/sigla estado):\t")

    usuarios.append({
        "nome": nome, 
        "data_nascimento": data_nascimento, 
        "cpf": cpf, 
        "endereco": endereco})
        
    print(f"Operação realizada com sucesso! Bem vindo, {nome}.")
    

def listar_contas(contas):
    separador = "=================================================="
    print(separador)
    for conta in contas:
        linha = f"\tAgência:\t{conta['agencia']}"
        linha += f"\n\tC\C:\t\t{conta['numero_conta']}"
        linha += f"\n\tTitular:\t{conta['usuario']['nome']}"
        print(linha)
        print(separador)   

def criar_conta(numero_conta, usuarios):
    cpf = input("Informe o CPF:\t")
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("\nConta criada com sucesso.")
            return {"agencia": "0001", "numero_conta": numero_conta, "usuario": usuario}
            
    print("\nEste CPF não foi cadastrado anteriormente. Operação cancelada.")
      
def main():

    saldo = 0
    extrato = ""
    usuarios = []
    numero_saques = 0
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "q":
            break
        
        elif opcao == "d":
            valor = float(input("Informe o valor do depósito:\t"))
	    
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float(input("Informe o valor do saque:\t"))
            
            saldo, extrato, numero_saques = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                numero_saques = numero_saques
            )
        
        elif opcao == "e":
            emitir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif opcao == "lc":
            listar_contas(contas)
            
        else:
            print("Operação inválida! Por favor certifique-se de que esteja selecionando a operação desejada e tente de novo.")

main()
