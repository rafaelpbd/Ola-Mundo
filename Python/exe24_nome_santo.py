'''
Crie um programa que leia o nome de uma cidade e diga se o primeiro nome começa com a palavra santo
'''
nome_cidade = input("\nDigite o nome de uma cidade: ")

nomeSeparado = nome_cidade.split()

if nomeSeparado[0].upper() == "SANTO":
    print('\nO primeiro nome da cidade é "Santo".\n')
else:
    print('\nO primeiro nome da cidade não é "Santo".\n')
