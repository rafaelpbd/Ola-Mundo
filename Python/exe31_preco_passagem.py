'''
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''

distancia = float(input("\nDigite a distância da viagem(km): \n"))

if distancia < 0:
    print("\nDistância inválida.\n")

elif 0 < distancia <= 200:
    precoPassagem = distancia * 0.5
    print("\nO preço da passagem será de R$ {:.2f}\n".format(precoPassagem))

else:
    precoPassagem = distancia * 0.45
    print("\nO preço da passagem será de R$ {:.2f}\n".format(precoPassagem))
