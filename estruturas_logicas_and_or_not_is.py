"""
 Estruturas Lógicas: and (e), or (ou), not (não), is (é).
 Operadores unários:
     - not, is
 Operadores Binários:
     - and, or
"""
ativo = False
logado = False

if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta, verifique seu e-mail.')


if ativo or logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta, verifique seu e-mail.')

if not ativo:
    print('Você precisa ativar sua conta, verifique seu e-mail.')
else:
    print('Bem-vindo usuário!')





