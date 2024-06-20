import textwrap
import re
from cliente import *
from conta import *
from historico import *
from menu import menu, menu_extrato
from transacao import Deposito

def encontrar_usuario(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def verificar_se_usuario_existe(clientes, precisa_retornar_cpf=False):
    cpf = input("Informe o CPF do cliente: ")
    cliente = encontrar_usuario(cpf, clientes)
    if not precisa_retornar_cpf:
        return cliente
    return cliente, cpf

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def pedir_data_nascimento():
    while True:
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        if validar_data(data_nascimento):
            return data_nascimento
        else:
            print("Data de nascimento no formato inválido! Tente novamente")

def validar_data(data):
    
    data_pattern = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
    
    if re.match(data_pattern, data):
        return True
    else:
        return False

def transferir(clientes, tipo):
    cliente = verificar_se_usuario_existe(clientes, precisa_retornar_cpf=False)

    if not cliente:
        print("\nCliente não encontrado!")
        return

    valor = float(input(f"Digite o valor para o {tipo}: "))
    
    if tipo == "deposito":
        tipo_transacao = Deposito
    elif tipo == "saque":
        tipo_transacao = Saque

    transacao = tipo_transacao(valor)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        print ("Cliente não possui uma conta.")
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cliente = verificar_se_usuario_existe(clientes, precisa_retornar_cpf=False)

    if not cliente:
        print("\nCliente não encontrado!")
        return
    
    conta = recuperar_conta_cliente(cliente)

    if not conta:
        print("\nCliente não possui uma conta.")
        return

    menu_extrato()
    transacoes = conta.historico.transacoes
    extrato = ""
    if not transacoes:
        extrato = "Nenhuma operação realizada até o momento."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao["tipo"]}:\n\tR${transacao["valor"]:.2f}"
    print(extrato)
    print(f"\nSaldo: \n\tR${conta.saldo:.2f}")

def criar_cliente(clientes):

    cliente, cpf = verificar_se_usuario_existe(clientes, precisa_retornar_cpf=True)

    if cliente:
        print("\nCliente já cadastrado com esse CPF!")
        return
    nome = input("Digite o nome completo do cliente: ")
    data_nascimento = pedir_data_nascimento()
    endereco = input("Digite o endereço do cliente: ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\nCliente cadastrado com sucesso!")

def criar_conta(numero_conta, clientes, contas):

    cliente = verificar_se_usuario_existe(clientes, precisa_retornar_cpf=False)

    if not cliente:
        print("\nNenhum cliente cadastrado com esse CPF!")
        return numero_conta
    
    numero_conta += 1
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print("Teste", cliente)

    print("\nConta criada com sucesso!")
    return numero_conta
    
def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))
    

def main():
    clientes = []
    contas = []
    numero_conta = 0

    while True:
        opcao = menu()

        if opcao == "1":
            transferir(clientes, "deposito")

        elif opcao == "2":
            transferir(clientes, "saque")
        
        elif opcao == "3":
            exibir_extrato(clientes)

        elif opcao == "4":
            criar_cliente(clientes)

        elif opcao == "5":
            numero_conta = criar_conta(numero_conta, clientes, contas)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

main()