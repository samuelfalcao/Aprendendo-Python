# Desafio - crie um programa que:
# - Escolhe um número secreto.
# - Pede por um chute do usuário.
# - Indica se o usuário acertou ou não.
# - Se não acertou, dá uma dica, dizendo
#   - se o número é mais alto ou mais baixo.
# - Repete isso até 3 vezes!

numero_secreto = 10
descobriu = False

for n in range(3):
    if not descobriu:
        chute = int(input('Descubra o número!\nSeu chute: '))
        if chute < numero_secreto:
            print('Chute muito baixo!')
        elif chute > numero_secreto:
            print('Chute muito alto!')
        else:
            print('Descobriu!')
            descobriu = True


if descobriu:
    print('Parabéns, você ganhou!')
else:
    print(f'Que pena, você perdeu! O número secreto era {numero_secreto}')

