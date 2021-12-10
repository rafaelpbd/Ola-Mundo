'''Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

km = float(input("\nQuantos km o carro percorreu? "))
dias = int(input("Por quantos dias o carro ficou alugado? "))
preco = (km * 0.15) + (dias * 60)

print("\nO preço do aluguel por {} dias e rodando {} km será de R$ {:.2f}.\n".format(dias, km, preco))