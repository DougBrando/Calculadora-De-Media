def obter_nota(mensagem):
    """Obtém uma nota do usuário, garantindo que seja um número válido e dentro do intervalo permitido."""
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Por favor, insira uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

def calcular_media(nota1, nota2):
    """Calcula a média de duas notas."""
    return (nota1 + nota2) / 2

def avaliar_media(media):
    """Avalia a média e retorna a situação do aluno."""
    if media > 7:
        return 'Você está APROVADO!'
    elif media == 7:
        return 'Você passou raspando.'
    elif media >= 5:
        return 'Você reprovou, vamos estudar mais.'
    elif media >= 3:
        return 'Você reprovou, vamos melhorar isso.'
    else:
        return 'REPROVADO.'

def main():
    while True:
        # Obtém as notas do usuário
        nota1 = obter_nota("Digite a primeira nota: ")
        nota2 = obter_nota("Digite a segunda nota: ")

        # Calcula a média
        media = calcular_media(nota1, nota2)

        # Exibe as notas e a média
        print("Suas notas foram {:.1f} e {:.1f}, sua média é de {:.1f}".format(nota1, nota2, media))

        # Avalia e exibe a situação do aluno
        resultado = avaliar_media(media)
        print(resultado)

        # Pergunta se o usuário deseja calcular novamente
        continuar = input("Deseja calcular novamente? (s/n): ").strip().lower()
        if continuar != 's':
            break

# Executa o programa
if __name__ == "__main__":
    main()
