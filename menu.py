import textwrap

# Função que imprime o menu principal
def menu():
    menu = '''\n
    {0:=^30}
    =={1:^26}==
    {0:=^30}

    Selecione uma opção:

    1. Depositar - Adicione fundos à sua conta.
    2. Sacar - Retire fundos da sua conta.
    3. Extrato - Verifique seu saldo atual.
    4. Criar Usuário - Adicione um novo cliente.
    5. Criar Conta - Adicone uma conta para um cliente.
    6. Listar Contas - Exibir uma lista de contas.
    0. Sair - Encerre o programa.

    Digite a opção escolhida: '''.format('', 'Menu Bancário')
    return input(textwrap.dedent(menu))


# Função que imprime o cabeçalho do extrato
def menu_extrato():
    menu_extrato = '''
    {0:=^30}
    =={1:^26}==
    {0:=^30}
    '''.format('', 'Extrato')
    return print(textwrap.dedent(menu_extrato))