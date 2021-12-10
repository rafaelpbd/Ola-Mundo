metros = float(input("Quantos metros deseja converter? "))

centi = metros * 100
mili = metros * 1000

print('''
{} metros em cm: {:.2f}
{} metros em mm: {:.2f}
'''.format(metros, centi, metros, mili))