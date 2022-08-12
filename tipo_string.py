"""
Tipo String.

Em Python um dado é considerado do tipo string sempre que:
- Estiver entre aspas simples -> 'uma string', '123', 'True'
- Estiver entre aspas dulpas ->"uma string, "123", "True"
- Estiver entre aspas triplas -> '''uma string''', '''123''', '''True'''

nome = 'Geek University'
print(nome)
print(type(nome))

nome= "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))
"""
"""
#Maiúsculo
nome ='Geek University'
print(nome)


#Minúscula
nome = 'Geek University'
print(nome.lower)
"""
#transforma em lista de strings
nome = 'Geek University'
print(nome.split())
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])

#[::-1] -> comece do primeiro elemento, vá até o ultimo e inverta.
print(nome[::-1])

# Substitui a letra 'e' por 'i' ou qualquer outra caso queira.
print(nome.replace('e', 'i'))











