#DECORADORES: permite ejecutar logica antes y despues de la funcion

PASSWORD = '12345'

#Ejemplo 1
def password_required(func):
    def wrapper():
        password = input('Cual es tu contraseña?')
        if password == PASSWORD:
            return func()
        else:
            print('La contraseña no es correcta')

    return wrapper

@password_required
def need_password():
    print('La contraseña es correcta')

#Ejemplo 2
def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper

@upper
def say_my_name(name):
    return 'Hola, {}'.format(name)

if __name__ == '__main__':
    print(say_my_name('David')
