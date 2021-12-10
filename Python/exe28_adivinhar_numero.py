'''
Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 1 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random

numero = random.randint(1,5)

numeroDig  = int(input("\nTenho um número em mente, entre 1 e 5, veja se você consegue adivinhar. Digite um número e veja se acertou: \n"))

if numeroDig == numero:
    print("Parabéns, você adivinhou o número. De fato eu estava pensando no número {}\n".format(numero))
else:
    print("Infelizmente você errou, o número que eu estava pensando era o {}\n".format(numero))
