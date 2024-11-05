# Calculadora de Média de Notas

Este programa em Python permite que o usuário insira duas notas e calcula a média, avaliando a situação do aluno com base nessa média. O programa inclui validação de entrada para garantir que as notas estejam dentro de um intervalo específico (0 a 10) e permite que o usuário faça múltiplos cálculos sem precisar reiniciar.

## Funcionalidades

- **Entrada de Notas**: Solicita ao usuário que insira duas notas, garantindo que sejam números válidos.
- **Cálculo da Média**: Calcula a média das duas notas inseridas.
- **Avaliação da Média**: Classifica o desempenho do aluno com base na média calculada:
  - Aprovado (média > 7)
  - Passou raspando (média == 7)
  - Reprovado, precisa estudar mais (média entre 5 e 7)
  - Reprovado, vamos melhorar isso (média entre 3 e 5)
  - Reprovado (média < 3)
- **Repetição do Processo**: Permite que o usuário faça novos cálculos sem reiniciar o programa.

## Como Usar

1. Execute o programa em um ambiente Python.
2. Insira a primeira e a segunda nota quando solicitado.
3. O programa exibirá suas notas, a média e a avaliação correspondente.
4. Você pode optar por calcular novas médias ou encerrar o programa.

## Exemplo de Uso

```plaintext
Digite a primeira nota: 8.5
Digite a segunda nota: 6.0
Suas notas foram 8.5 e 6.0, sua média é de 7.3
Você reprovou, vamos estudar mais.
Deseja calcular novamente? (s/n): s
```

## Requisitos
Python 3.x
