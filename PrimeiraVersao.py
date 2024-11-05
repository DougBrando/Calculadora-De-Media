# Solicita ao usuário que digite as duas notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média das notas
media = (nota1 + nota2) / 2

# Exibe as notas e a média formatadas
print("Suas notas foram {:.1f} e {:.1f}, sua média é de {:.1f}".format(nota1, nota2, media))

# Avalia a situação do aluno com base na média
if media > 7:
    print('Você está APROVADO!')
elif media == 7:
    print('Você passou raspando.')
elif media >= 5:
    print('Você reprovou, vamos estudar mais.')
elif media >= 3:
    print('Você reprovou, vamos melhorar isso.')
else:
    print('REPROVADO.')
