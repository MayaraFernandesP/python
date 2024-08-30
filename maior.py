n1 = int (input('Digite um número: '))
n2 = int (input('Digite o segundo núemro: '))

def maior_numero(n1, n2):
    if n1> n2:
        return n1
    else: 
        return n2

print('O maior número é {}!'.format(maior_numero(n1, n2)))