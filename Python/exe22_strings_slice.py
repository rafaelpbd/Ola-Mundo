'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
Nome com todas as letras maiusculas
Nome com todas as letras minusculas
Quantas letras ao todo, sem espaços
Quantas letras tem o primeiro nome
'''
nome = input("Digite seu nome completo: ")
nomeSeparado = nome.split()
nomeJunto = "".join(nomeSeparado)

print('''
Nome maiusculo: {}
Nome minusculo: {}
Possui {} letras 
O primeito nome possui {} letras   
'''.format(nome.upper(), nome.lower(), nomeJunto.__len__(), nomeSeparado[0].__len__()))

