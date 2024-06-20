from cliente import *
from conta import *
from historico import *
from transacao import *

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        acima_saldo = valor > self._saldo
        valor_negativo = valor < 0
        if acima_saldo:
            print("\nFalha ao realizar o saque! Saldo insuficiente.")
            return False
        elif valor_negativo:
            print("\nFalha ao realizar o saque! Valor de saque não permitido.")
            return False
        else:
            self._saldo -= valor
            print(f"Valor de R${valor:.2f} sacado com sucesso!")
            return True

    def depositar(self, valor):
        valor_negativo = valor < 0
        if valor_negativo:
            print("\nFalha ao realizar o depósito! Valor de depósito não permitido.")
            return False
        else:
            self._saldo += valor
            print(f"Valor de R${valor:.2f} depositado com sucesso!")
            return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques= limite_saques
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\nFalha ao realizar o saque! Valor excedeu o limite permitido.")
        elif excedeu_saques:
            print("\nFalha ao realizar o saque! Número de saques diários excedeu o limite permitido.")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""
            Agência: \t{self.agencia}
            C/C: \t\t{self.numero}
            Titular: \t{self.cliente.nome}
        """