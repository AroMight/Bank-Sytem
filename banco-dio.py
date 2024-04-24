from datetime import datetime


def normalizar_valor(valor):
    '''Função para normalizar o valor inserido pelo usuário.'''
    try:
        valor_limpo = float(valor)
        return valor_limpo
    except ValueError:
        return None


def agora():
    '''Função para retornar a data e hora das operações.'''
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return agora


class Conta:

    LIMITE_SAQUE = 500

    def __init__(self):
        self.saldo = 0
        self.saques_restantes = 3
        self.extrato = []

    def depositar(self, valor):
        '''Método para depositar um valor na conta.'''
        valor_deposito = normalizar_valor(valor)
        if valor_deposito is not None and valor_deposito > 0:
            self.saldo += valor_deposito
            self.extrato.append(f'{agora()}: depósito no valor de R$ {valor_deposito:.2f}')
            print(f'Operação realizada com sucesso. Você depositou R${
                  valor_deposito:.2f}!\n')
        else:
            print(
                'Não foi possível finalizar a operação. Por favor, escolha um valor válido para depósito.\n')

    def sacar(self, valor):
        '''Método para sacar um valor da conta.'''
        valor_saque = normalizar_valor(valor)
        if valor_saque is not None and valor_saque > 0:
            if self.saques_restantes == 0:
                print(
                    'Você alcançou o limite de 3 saques por dia. Por favor, tente outro dia.')
            elif valor_saque > self.saldo:
                print(
                    'Não foi possível realizar a operação. Você não possui saldo suficiente.')
            elif valor_saque > self.LIMITE_SAQUE:
                print(
                    f'O limite máximo para cada saque é de R$ {
                        self.LIMITE_SAQUE}.'
                )
            else:
                self.saldo -= valor_saque
                self.saques_restantes -= 1
                self.extrato.append(f'{agora()}: saque no valor de R$ {valor_saque:.2f}')
                print(f'Operação realizada com sucesso. Você sacou R${
                      valor_saque:.2f}!')
        else:
            print(
                f'Não foi possível finalizar a operação. Por favor, escolha um valor válido para depósito.')

    def emitir_extrato(self):
        '''Método para exibir o extrato da conta.'''
        if self.extrato == []:
            print('Não há operações para exibir.\n')
        else:
            print('\033[33mExtrato\033[m')
            for operacao in self.extrato:
                print(operacao)


if __name__ == '__main__':

    conta = Conta()

    while True:
        opcao = input('''\033[32mBem-vindo ao Banco DIO!\033[m
          \033[32m[1]\033[m Depositar
          \033[32m[2]\033[m Sacar
          \033[32m[3]\033[m Extrato
          \033[32m[4]\033[m Sair
          >>>''')

        if opcao == '1':
            valor = input('Digite o valor que deseja depositar: ')
            conta.depositar(valor)

        elif opcao == '2':
            valor = input('Digite o valor que deseja sacar: ')
            conta.sacar(valor)

        elif opcao == '3':
            conta.emitir_extrato()

        elif opcao == '4':

            print('Obrigado por utilizar o Banco DIO!')
            break

        else:
            print('Opção inválida. Por favor, tente novamente.')
