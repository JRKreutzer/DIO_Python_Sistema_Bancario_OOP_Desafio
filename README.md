# Sistema Bancário com Classes

Este é um código desenvolvido como parte do desafio proposto pelo Bootcamp Python Backend da Digital Innovation One. Trata-se de um programa simples de console em Python que simula algumas operações bancárias básicas, como depósito, saque e verificação de extrato, nesse desafio em particular, foram criadas classes para aplicar os conhecimentos adquiridos durante os cursos de OOP, entre eles herença, encapsulamento, polimorfismo, interfases e classes abstratas. 
## Funcionalidades

1. **Depositar:** Permite ao usuário adicionar fundos à sua conta bancária.
2. **Sacar:** Permite ao usuário retirar fundos da sua conta bancária, com a devida validação do saldo e do limite de saque diário.
3. **Extrato:** Mostra ao usuário o saldo atual da conta, bem como o registro de todas as transações realizadas.
4. **Criar Usuário - Adiciona um novo cliente.
5. **Criar Conta - Adicona uma conta para um cliente.
6. **Listar Contas - Exibe uma lista de contas.
0. **Sair:** Encerra o programa.

## Diagrama base

![Diagrama disponibilizado pela DIO](https://github.com/JRKreutzer/DIO_Python_Sistema_Bancario_OOP_Desafio/blob/main/Trilha%20Python%20-%20desafio.png)

## Requisitos

- Python 3.x instalado no sistema.

## Como Usar

1. Clone este repositório ou faça o download dos arquivos `cliente.py`, `conta.py`, `historico.py`, `menu.py`, `transacao.py` e `sistemas_bancario.py` (todos devem ser colocados na mesma pasta).
2. Abra um terminal ou prompt de comando.
3. Navegue até o diretório onde o arquivo `sistemas_bancario.py` está localizado.
4. Execute o seguinte comando: python sistemas_bancario.py
5. Siga as instruções apresentadas no console para realizar as operações desejadas.

## Observações

- Certifique-se de inserir apenas valores válidos ao realizar depósitos e saques.
- O limite de saques diários é configurado para 3, mas pode ser ajustado alterando a variável `LIMITE_SAQUES`.
- O limite de saque por transação é de R$ 500,00, mas também pode ser alterado, se necessário, modificando a variável `limite`.
- As mensagens de erro e confirmação foram projetadas para orientar o usuário durante a interação com o programa.
- Não é permitido criar usuários com um mesmo CPF
- Um usuário pode ter várias contas
- Certifique-se de digitar uma data de nascimento válida no formato xx-xx-xxxx

Este programa foi desenvolvido como uma demonstração educacional e não deve ser utilizado para transações financeiras reais.

## Autor

Desenvolvido por José Rodolfo Kreutzer - [jose.kreutzer@gmail.com]

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar sugestões de melhorias, relatar problemas ou enviar solicitações de pull requests.
