
def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuario')

loginUsuario('Admin')
loginUsuario('User')
