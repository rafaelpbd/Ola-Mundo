metros = float(input("Digite quantos metros deseja converter: "))

print('''
{:.2f} m em:

micrometro (μm): {} 
milimetro (mm): {:.2f}
centimetro (cm): {:.2f}
decímetro (dm): {}
decametro (dam): {}
hectometro (hm): {}
quilometro (km): {}
'''.format(metros, (metros * 1000000), (metros * 1000), (metros * 100), (metros * 10), (metros / 10), (metros / 100), (metros / 1000)))
