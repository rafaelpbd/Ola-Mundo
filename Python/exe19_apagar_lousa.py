import random

num_aleatorio = random.randint(0,3)
nomes_alunos = ["Aline", "Marcos", "Julia", "Anderson"]

if num_aleatorio == 0 or num_aleatorio == 2:
    print("\nA aluna sorteada para apagar a lousa é a {}\n".format(nomes_alunos[num_aleatorio]))
else:
    print("\nO aluno sorteado para apagar a lousa é o {}\n".format(nomes_alunos[num_aleatorio]))

