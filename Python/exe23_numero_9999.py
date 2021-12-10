'''
Crie um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
'''
numero = input("Digite um numero entre 0 e 9999: ")

if numero.__len__() < 1 or numero.__len__() > 4:
    print('''
Número inválido
''')

elif numero.__len__() == 4:
    print('''
Milhar: {} Centena: {} Dezena: {} Unidade: {}
'''.format(numero[0], numero[1], numero[2], numero[3]))

elif numero.__len__() == 3:
    print('''
Milhar: 0 Centena: {} Dezena: {} Unidade: {}
'''.format(numero[0], numero[1], numero[2]))

elif numero.__len__() == 2:
    print('''
Milhar: 0 Centena: 0 Dezena: {} Unidade: {}
'''.format(numero[0], numero[1]))

elif numero.__len__() == 1:
    print('''
Milhar: 0 Centena: 0 Dezena: 0 Unidade: {}
'''.format(numero[0]))

