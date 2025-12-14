# Desafio - crie um programa que:
# - Pede por um nome de usuário e uma senha.
# - Se ambos forem corretos, exibe uma mensagem de sucesso.
# - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
# quando o usuário está incorreto, e quando a senha está incorreta
# - O usuário/senha "corretos" podem ser definidos como
# variávies dentro do próprio código.

usuario_correto = 'Pedro'
senha_correta = 'senha secreta'

usuario = input('Nome de usuário: ')
senha = input('Senha: ')

if usuario == usuario_correto:
    if senha == senha_correta:
        print(f'Acesso liberado, seja bem-vindo {usuario}!')
    else:
        print(f'Senha incorreta para o usuário {usuario}.')
else:
    print(f'Usuario {usuario} não cadastrado no sistema')

