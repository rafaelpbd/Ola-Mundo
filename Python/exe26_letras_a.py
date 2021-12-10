'''
Crie um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra a
Em que posição ela aparece pela primeira vez
Em que posição ela aparece pela última vez
'''
nome = input("\nDigite uma frase: ")
nome = nome.lower().strip()


print('''
A letra "A" aparece {} vezes nessa frase, primeiro na posição {} e por último na posição {}.

'''.format(nome.count("a"), nome.find("a") + 1, nome.rfind("a") +1 ))
