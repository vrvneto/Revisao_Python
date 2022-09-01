"""
LISTAS

- Listas em python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e tambem de podermos colocar qualquer tipo de dado.

- Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando
elementos; Não possuem tipo de dado fixo.

- As listas em Python são representadas por colchetes: [].
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 45, 42, 27]

lista2 = ['g', 'h', 'b', 'y', 't', 'k', 'l', 'q', 'r']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido na lista.
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
# lista1.append(12, 34, 56) # Erro
lista1.append([8, 3, 1])  # coloca como elemento único (sublista)
print(lista1)
if 22 in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

# Extend adiciona mais de um elemento a lista.
lista1.extend([123, 44, 67])
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do ídice (INSERT)
lista1.insert(2, 'Novo Valor')
print(lista1)
# OBS: não substitui o valor, apenas desloca para a direita

# Podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6) # OBS pode ser feito com extend lista1.extend(lista2)

# Podemos facilmente inverter uma lista (REVERSE)
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

#Podemos Copiar uma lista (COPY)
lista6 = lista2.copy()
print(lista6)

# Contar elementos de uma lista (len)
print(len(lista5))

#Podemos remover facilmente o ultimo elemento de uma lista (pop)
print(lista5)
lista5.pop()
print(lista5)
lista5.pop()
print(lista5)
# Podemos Remover um elemento pelo indice
lista5.pop(2)
print(lista5) # OBS: Os elementos a direita serão deslocados para a esquerda

#Podemos remover todos os elementos(clear)
lista5.clear()
print(lista5)

# Podemos repetir elementos em uma lista
lista5 = [1, 2, 3]
print(lista5)
lista5 = lista5 * 3
print(lista5)

# Podemos converter uma string em lista
# Exemplo 1
curso = 'Programação em Python'
print(curso)
curso = curso.split()
print(curso)

# Podemos converter uma lista em string
curso = ' '.join(curso)
print(curso)
""" 
# Iterando sobre listas
# Exemplo 1 utilizando for
for elemento in lista1:
    print(elemento)
# Exemplo 2 utilizando while
carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)
"""
# Podemos fazer acesso aos elementos de forma indexada
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Encontrar o indice de um elemento na lista
numeros = [5, 7, 6, 8, 56, 43, 61, 12, 19, 13, 23, 31, 35, 44, 46, 34, 51, 24, 39]

# Em qual indice está o valor 31?
print(numeros.index(31))
# Em qual indice está o valor 24?
print(numeros.index(24))
# OBS: Caso não tenha o lemento na lista será considerado erro (ValueError)

# Ordenar lista 'numeros'
numeros.sort()
print(numeros)

# Revisão de Slicing
# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# trabalhando com slice de lista com o parametro 'inicio'

print(numeros[1:]) # iniciando do indice 1 e pegando todosm os restantes

# trabalhando com slice de lista com o parâmetro 'fim'
print(numeros[:14])

# Trabalhando com slice de lista com o parâmetro ´passo´
print(numeros[0::3]) # Começa do indice 0 e vai de 3 em 3

# Soma*, Valor Maximo*, Valor Mínimo*, tamanho.
print(sum(numeros))    # soma
print(max(numeros))    # máximo valor
print(min(numeros))    # mínimo valor
print(len(numeros))    # tamanho da lista


# Transformar uma lista em tupla
print(type(numeros))
tupla = tuple(numeros)
print(tupla)
print(type(numeros))

