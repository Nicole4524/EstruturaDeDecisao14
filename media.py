'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
'''
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
media = (nota1 + nota2) /2

if media >= 9.0 and media <= 10:
    print("Sua média é de:", media)
    print("Parabéns, nota: A")
    print("Você foi aprovado!")

elif media >= 7.5 and media< 9:
    print("Sua média é de:", media)
    print("Nota: B")
    print("Você foi aprovado!")

elif media >= 6.0 and media < 7.5:
    print("Sua média é de:", media)
    print("Nota: C")
    print("Você foi aprovado!")

elif media >= 4.0 and media < 6.0:
    print("Sua média é de:", media)
    print("Nota: D")
    print("Você foi reprovado!")

elif media >= 0.0 and media < 4.0:
    print("Sua média é de:", media)
    print("Nota: E")
    print("Você foi reprovado!")


else:
    print("Nota inválida")