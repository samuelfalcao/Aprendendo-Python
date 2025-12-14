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
usuario_esta_correto = usuario == usuario_correto
senha_esta_correta = input('Senha: ') == senha_correta

if usuario_esta_correto and senha_esta_correta:
    print(f'Acesso liberado, seja bem-vindo {usuario}!')
if usuario_esta_correto and not senha_esta_correta:
    print(f'Senha incorreta para o usuário {usuario}.')
if not usuario_esta_correto:
    print(f'Usuário {usuario} não cadastrado no sistema')

