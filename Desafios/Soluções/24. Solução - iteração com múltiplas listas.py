# Dado duas listas, printe todos os valores que aparecerem
# duplicados nas duas listas.

valores1 = [2, 4, 6]
valores2 = [1, 2, 6, 8]

for valor1 in valores1:
    for valor2 in valores2:
        if valor1 == valor2:
            print(f'Valor {valor1} aparece nas duas listas')

print('\n\n')

# Dado duas listas, printe uma mensagem dizendo se existe
# algum elemento em comum entre elas ou não.

lista1 = [10.0, 'xxx', True]
lista2 = [0, False, 'xxx']

elemento_em_comum = False

for valor1 in lista1:
    if elemento_em_comum:
        break
    for valor2 in lista2:
        if valor1 == valor2:
            elemento_em_comum = True
            break

if elemento_em_comum:
    print(f'As listas {lista1} e {lista2} possuem elementos em comum')
else:
    print(f'As listas {lista1} e {lista2} NÃO possuem elementos em comum')
