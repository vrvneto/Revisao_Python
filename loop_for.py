"""
Loop For

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

Python
for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # temos que transformar em uma lista

# Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando em uma lista)
for numero in lista:
    print(numero)


# Exemplo de for 3 (iterando em um range)
for numero in range(1, 10):
    print(numero)
"""
Enumerate:
((0, 'G'), (1, 'e')...)

for i, v in enumerate(nome:)
    print(nome[i])
"""

qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f"A soma é {soma}")





