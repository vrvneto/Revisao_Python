"""
Loop While

Forma geral:

While expressão_booleana:
    //execução do loop

O bloco do while deve ser repetido enquanto a expressão booleana for verdadeira.

-Expressão booleana é toda expressão onde o resultado é True ou False.

"""
# Exemplo 1
numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1
# enquanto 'numero' menor que 10 vai ser impresso 'numero'.
# OBS: Em um loop while é necessário um critério de parada (tem que ser finito)

# Exemplo 2
resposta = ''

while resposta != "sim":
    resposta = input('Já acabou Jéssica? ')
# Enquanto 'resposta' for diferente de 'sim' pergunta novamente.



