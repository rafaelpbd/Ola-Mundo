from math import cos, sin, degrees, radians

angulo = float(input("\nDigite o valor de um ângulo qualquer: "))
seno = sin(angulo)
cosseno = cos(angulo)
print("\nO seno de {} é {:.3f} e o cosseno é {:.3f}\n".format(angulo, seno, cosseno))
