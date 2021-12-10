'''
Crie um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o último nome separadamente

'''
nome = input("\nDigite um nome completo: ")
nome = nome.split()

print('''
O primeiro nome é {} e o último nome é {} 
'''.format(nome[0], nome[(nome.__len__()) - 1]))
