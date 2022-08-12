"""
escopo de variáveis.
Dois casos de escopo:

1 - Variáveis globais;
    - Variáveis globais sáo reconhecidas, ou seja, seu escopo compreende todo o programa.

2 - Variáveis Locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Para declarar variáveis emk Python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não
colocamos o tipo de dado dela. Este tipo é inferido ao atribuírmos o valor a mesma.

"""
# Exemplo de variável global:
numero = 42
print(numero)

#Exemplo de variável local:
if numero > 10:
    novo = numero + 10  # A variável 'novo' esta localmente dentro do if.
    print(novo)
