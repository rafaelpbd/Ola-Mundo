largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = altura * largura
tinta = area / 2.0

print("A area da parede é {:.2f} m2 e a quantidade de tinta necessária para pintar essa parede será de {:.2f} L.".format(area, tinta))
