"""
Range

- Precisamos conhecer loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatoria,
mas sim de maneira especificada.

Formas gerais:
- range (valor_de_parada)
OBS: valor_de_parada não inclusive(início padrão 0, e passo de 1 em 1)

"""

# Forma 1
for num in range(11): #range( vai de 0 ate o valor_de_parada)
    print(num)

# Forma 2
for num in range(4, 11): # range(valor_de_inicio, valor_de_parada)
    print(num)

# Forma 3
for num in range(3, 13, 3): # range(valor_de_inicio, valor_de_parada, e passo especificado pelo usuário)
    print(num)

# Forma 4 (inversa)
for num in range(10, -1, -1): # range(valor_de_inicio, valor_de_parada, e passo especificado pelo usuário)
    print(num)
    