din = float(input("Quantos Reais deseja converter para dólar? "))

print('''
Com R$ {:.2f} você consegue comprar $ {:.2f} Dólares americanos.

'''.format(din, din / 5.51))