from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('============================================================')
    print('=========================ATM================================')
    print('=====================BANCO FORTUNA==========================')
    print('=====================SEJA BEM VINDO=========================')
    print('============================================================')

    print('Em que posso ajudar?')
    print('1 - Criar Conta')
    print('2 - Efetuar Saque')
    print('3 - Efetuar Depósito')
    print('4 - Efetuar Transferência')
    print('5 - Efetuar Pagamento')
    print('6 - Listar Contas')
    print('7 - Sair')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()

    elif opcao == 2:
        efetuar_saque()

    elif opcao == 3:
        efetuar_deposito()

    elif opcao == 4:
        efetuar_transferencia()

    elif opcao == 5:
        pagar()

    elif opcao == 6:
        listar_contas()

    elif opcao == 7:
        print('Obrigado e volte sempre!')
        sleep(1)
        exit(0)

    else:
        print('Opção Inválida')
        sleep(1)
        menu()


def criar_conta() -> None:
    print('Informe os dados do cliente')

    nome: str = input('Nome do Cliente')
    rg: str = input('RG')
    cpf: str = input('CPF')
    data_nascimento: str = input('Data de Nascimento')
    email: str = input('E-Mail')

    cliente: Cliente = Cliente(nome, rg, cpf, data_nascimento, email)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso!')
    print('Dados da Conta: ')
    print('--------------------------')
    print(conta)
    sleep(1)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta'))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)

        else:
            print(f'Não foi encontrada a conta com número {numero}')

    else: print('Não existem contas cadastradas!')
    sleep(1)
    menu()

def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta'))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito:'))

            conta.depositar(valor)

        else:
            print(f'Não foi encontrada a conta com número {numero}')

    else: print('Não existem contas cadastradas!')
    sleep(1)
    menu()

def pagar() -> None:
    if len(contas) > 0:
        numero_p: int = int(input('Informe o número da conta'))

        conta_p: Conta = buscar_conta_por_numero(numero_p)

        if conta_p:
            numero_r: int = int(input('Informe o código de barras! '))

            conta_r: Conta = buscar_conta_por_numero(numero_r)

            if conta_r:
                valor: float = float(input('Informe o valor a ser pago! '))

                conta_p.transferir(conta_r, valor)

            else:
                print(f'Não foi encontrada a conta com número {numero_r}')


        else:
            print(f'Não foi encontrada a conta com número {numero_p}')

    else:
        print('Não existem contas cadastradas!')
    sleep(1)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da conta'))

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input('Informe número da conta destino! '))

            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informe o valor da transferência! '))

                conta_o.transferir(conta_d, valor)

            else:
                print(f'Não foi encontrada a conta com número {numero_d}')


        else:
            print(f'Não foi encontrada a conta com número {numero_o}')

    else: print('Não existem contas cadastradas!')
    sleep(1)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Lista de Contas')

        for conta in contas:
            print(conta)
            print('-------------------------')
            sleep(3)


    else:
        print('Não existem contas cadastradas!')
        sleep(1)
        menu()

def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()

