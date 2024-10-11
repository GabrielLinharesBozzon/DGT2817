
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Nao foi possivel realizar a divisao por 0"
    return a / b

def calculadora(a, b, operacao):
    if operacao == '+' or operacao == 'adicao':
        return adicao(a, b)
    elif operacao == '-' or operacao == 'subtracao':
        return subtracao(a, b)
    elif operacao == '*' or operacao == 'multiplicacao':
        return multiplicacao(a, b)
    elif operacao == '/' or operacao == 'divisao':
        return divisao(a, b)
    else:
        return 'Operacao invalida'

saida = ''

while saida.lower() != 'n':
    a = float(input('Digite o primeiro numero: '))
    b = float(input('Digite o segundo numero: '))
    operacao = input('Digite a operacao desejada (+, -, *, /): ')
    resultado = calculadora(a, b, operacao)
    print('Resultado da operacao: ' + str(resultado))
    
    saida = input('Deseja continuar? (S/N): ')
