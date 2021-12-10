'''
Crie um programa que leia o nome de uma pessoa e diga se o nome contém silva.
'''
nome = input("\nDigite o nome completo de uma pessoa: ")

if nome.lower().__contains__("silva"):
    print('\nO nome digitado contém o nome Silva nele.\n')
else:
    print('\nO nome digitado não contém o nome Silva nele.\n')
