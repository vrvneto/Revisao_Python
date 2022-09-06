"""
- Tuplas (tuple)

Tuplas são bem parecidas com listas, existem duas diferenças básicas:
- As tuplas são representadas por parenteses ()
- As tuplas são imutáveis, ao se criar uma tupla ela não muda. toda operação
  em uma tupla gera uma nova tupla.

"""
# CUIDADO 1: as tuplas são representadas por parenteses, mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4)# Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,)
print(tupla4) # Isso é uma tupla
print(type(tupla4))

tupla5 = 5,
print(tupla5)
print(type(tupla5))

# CONCLUSÂO: Podemos concluir que tuplas são definidas pela virgula e não pelo parenteses

# Tupla pode ser criada por um 'range'.
tupla6 = tuple(range(11))
print(tupla6)
print(type(tupla6))

