"""
LISTAS

- Listas em python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e tambem de podermos colocar qualquer tipo de dado.

- Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a lista e simplismente ir adicionando
elementos; Não possuem tipo de dado fixo.

- As listas em Python são representadas por colchetes: [].
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 45, 42, 27]

lista2 = ['g', 'h', 'b', 'y', 't', 'k', 'l', 'q', 'r']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido n lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ORDENAR uma lista usando 'SORT'.
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrencias de um valor em uma lista usando 'COUNT'.
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas utilizamos a função 'APPEND'.
print(lista1)
lista1.append(42)
print(lista1)
# OBS: com append só é possível passar um elemento por vez.

