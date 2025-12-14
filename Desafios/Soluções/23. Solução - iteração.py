# Dado uma sequência de números, calcule a soma e média dos números.
# ATENÇÃO: não vale usar a função sum() !

valores = [10, 30, 10, 10, 10]

soma = 0
for valor in valores:
    soma += valor

media = soma / len(valores)

print(f'A soma dos valores {valores} é: {soma}')
print(f'A média dos valores {valores} é: {media}')

print('\n\n')

# Dado uma sequência de números, calcule o maior valor da sequência.
# ATENÇÃO: não vale usar a função max() !

valores = [10, 30, 10, 10000, 10]

maximo = valores[0]
for valor in valores:
    if valor > maximo:
        maximo = valor

print(f'O valor máximo dos valores {valores} é: {maximo}')

print('\n\n')

# Dado uma lista de palavras, printe todas as palavras
# com pelo menos 5 caracteres.

palavras = ['oi', 'Python', 'Programação', 'xxx']
for palavra in palavras:
    if len(palavra) >= 5:
        print(f'Encontrada palavra com 5+ caracteres: {palavra}')
