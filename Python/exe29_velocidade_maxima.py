'''
Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocidade = float(input("\nDigite a velocidade do carro: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("\nVocê foi multado. O valor da multa será de R$ {:.2f}.\n".format(multa))

else:
    print("\nA velocidade está de acordo com a velocidade limite.\n")
