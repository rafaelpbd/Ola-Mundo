import math


cat_oposto = float(input("\nDigite o catesto oposto: "))
cat_adjacente = float(input("\nDigite o catesto adjacente: "))
hipotenusa = pow(cat_oposto, 2) + pow(cat_adjacente, 2)

print("\nA Hipotenusa é {:.2f}\n".format(math.sqrt(hipotenusa)))
