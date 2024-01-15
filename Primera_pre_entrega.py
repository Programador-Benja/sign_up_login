# Registro de usuarios
# Se debe guardar el nombre de usuario y contraseña
# Se guarda y muestra la informacion mediante funciones
# Usar un diccionario para guardar el par user-password(clave,valor)
# Crear una funcion para el login de usuarios, comprobando que coincida la contraseña y el usuario
# Guardar en un archivo de texto los datos

usuarios = {}

def bienvenida():
    print("\n¡Bienvenido a mi programa!\n")

def registro_de_usuarios(user):
    bienvenida()
    print("\tSign up")
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    
    user[usuario] = contraseña

def leer_registros(user):
    for nombre, contraseña in user.items():
        print(f"{nombre} : {contraseña}")

def guardar_archivo(user):
    file = open("base_de_datos.txt","w")
    file.write("\t Usuarios registrados en la APP\n")

    for nombre, contraseña in user.items():
        file.write(f"{nombre} : {contraseña}\n")
    
    file.close()

def iniciar_sesion(users):
    print("\n \tLogin")
    usuario = input("Ingrese su usuario: ")

    for user, password in users.items():
        if usuario == user:
            contraseña = input("Ingrese su contraseña: ")
            if contraseña == password:
                print(f"\nBienvenido/a {usuario}")
            else:
                print("\nContraseña incorrecta!")
        else:
            print("\nUsuarion no encontrado!")

# Se registran los usuarios por medio de la funcion registro_de_usuarios()
registro_de_usuarios(usuarios)

# Se muestra en pantalla los registros de los usuarios con sus contraseñas
leer_registros(usuarios)

# Se guarda en un archivo txt los registros de los usuarios
guardar_archivo(usuarios)

# Se accede a la plataforma mediante un login llamando a la funcion iniciar_sesion()
iniciar_sesion(usuarios)