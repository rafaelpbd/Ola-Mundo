import random

num_aleatorio = -1
num_sort = []
nomes_alunos = ["Aline", "Marcos", "Julia", "Anderson"]
i = 0

while i < 4:
    num_aleatorio = random.randint(0,3)
    if num_aleatorio not in num_sort:
        num_sort.append(num_aleatorio)
        i = i + 1


print('''
A ordem de apresentação será a seguinte:

{}
{}
{}
{}
'''.format(nomes_alunos[num_sort[0]], nomes_alunos[num_sort[1]], nomes_alunos[num_sort[2]], nomes_alunos[num_sort[3]]))
