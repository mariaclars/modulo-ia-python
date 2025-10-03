#2 - Criar um código que registre as notas de alunos e calcular a média da turma.

soma = 0

serie = int(input("\nDigite o numero da série: "))
qnt_alunos = int(input("Quantos alunos tem na turma? "))


for aluno in range(qnt_alunos):
    nome_aluno = input("\nNome do aluno? ")
    nota = float(input("Nota final do aluno: "))
    
    soma += nota

media = soma / qnt_alunos
print(f"A turma {serie} tem {qnt_alunos} e a media de suas notas é {media:.1f}.")