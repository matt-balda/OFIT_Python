import argparse
import logging


def soma(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def multi(a: int, b: int) -> int:
    if ((a or b) == 0):
        return 0
    return a * b


def div(a: int, b: int) -> int:
    if (b == 0):
        return logging.error('O divisor não pode ser 0')
    return a / b


def main():
    # Aqui estamos definindo o nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(description='Calculadora simplista')
    # O objeto 'parser' é uma instância da classe 'ArgumentParser' do módulo 'argparse'
    # Esta classe é utilizada para definir argumentos de linha de comando
    # Como no exemplo abaixo, o argumento '-a' é definido como um número flutuante

    # parser.add_argument('-a', type=int, help='Primeiro número para a operação')
    # parser.add_argument('-b', type=int, help='Segundo número para a operação')

    # Aqui será extraído os valores da linha de comando
    # args = parser.parse_args()
    # O objeto 'args' é uma instância da classe 'Namespace'
    # Esta classe é utilizada para armazenar os valores dos argumentos
    # Como no exemplo abaixo, o valor do argumento '-a' é acessado através de 'args.a'

    # while True:
    a = int(input('Digite o primeiro valor: '))
    b = int(input('Digite o segundo valor: '))
    # if a.isnumeric() and b.isnumeric():
    #   break
    # else:
    #   continue

    logging.info(' Valor de a: %s', a)

    operation = input('1: +, 2: -, 3: *, 4: /')

    # Em Python não há switch/case, mas podemos utilizar o 'if' para verificar valores
    result = None  # O valor 'None' é utilizado para representar um valor nulo
    if operation == '1':
        # Aqui é chamada a função 'soma' definida acima
        # O valor retornado pela função é armazenado na variável 'result'
        result = soma(a, b)
    elif operation == '2':

        result = sub(a, b)
    elif operation == '3':
        result = multi(a, b)
    elif operation == '4':
        result = div(a, b)
    else:
        logging.error('Operação inválida: %s', operation)
        return

    logging.info('Resultado: %s', result)


if __name__ == '__main__':

    main()
