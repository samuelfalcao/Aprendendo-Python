# Desafio - crie um programa que:
# - Pede pelo seu nome e idade
# - Dá oi para você
# - Conta quantas letras seu nome possui
# - Fala quantos anos você terá daqui a 5 anos

# Pega inputs do usuário
nome = input("Qual o seu nome?")
idade = input("Qual a sua idade?")

# Faz conversões de idade
idade_futuro = int(idade) + 5
idade_futuro_str = str(idade_futuro)

# Exibe resultados do código
print('Olá, ' + nome + "!")
print('Seu nome tem ' + str(len(nome)) + ' letras.')
print('Daqui 5 anos, você terá ' + idade_futuro_str + ' anos.')

