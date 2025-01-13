# Función para leer un archivo
def leer_archivo(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
    return lineas

# Función para calcular el puntaje de seguridad de una contraseña
def calcular_puntaje(password, lineasOdvios, minusculas, mayusculas, numeros):
    puntuacion = 0
    existeMinus = False
    existeMayus = False
    existeNums = False
    existeSimbols = False
    simbolosExtra = 0

    for caracter in password.strip():
        puntuacion += 1
        if not existeMinus and caracter in minusculas:
            puntuacion += 1
            existeMinus = True
        if not existeMayus and caracter in mayusculas:
            puntuacion += 1
            existeMayus = True
        if not existeNums and caracter in numeros:
            puntuacion += 1
            existeNums = True
        if caracter not in minusculas and caracter not in mayusculas and caracter not in numeros:
            if not existeSimbols:
                puntuacion += 3
                existeSimbols = True
            else:
                simbolosExtra += 1

    puntuacion += simbolosExtra * 2

    for patrones in lineasOdvios:
        patrones = patrones.strip() 
        if password == patrones:
            puntuacion -= 5
            break

    return puntuacion

# Función para clasificar una contraseña según su puntaje
def clasificar_contraseña(puntuacion):
    if puntuacion <= 15:
        return "Debil"
    elif puntuacion > 15 and puntuacion <= 20:
        return "Moderada"
    elif puntuacion > 20 and puntuacion <= 35:
        return "Buena"
    elif puntuacion > 35 and puntuacion <= 100:
        return "Excelente"
    else:
        return "Impenetrable"

# Función para ordenar contraseñas según su puntaje
def ordenar_contraseñas(listaDeContraseñasPuntuadas):
    for i in range(len(listaDeContraseñasPuntuadas)):
        for j in range(0, len(listaDeContraseñasPuntuadas) - i - 1):
            if listaDeContraseñasPuntuadas[j][1] < listaDeContraseñasPuntuadas[j + 1][1]:
                listaDeContraseñasPuntuadas[j], listaDeContraseñasPuntuadas[j + 1] = listaDeContraseñasPuntuadas[j + 1], listaDeContraseñasPuntuadas[j]
    return listaDeContraseñasPuntuadas

# Función para exportar el archivo con contraseñas clasificadas
def exportar_archivo(nombre_archivo, listaDeContraseñasPuntuadas):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for password, puntuacion, categoria in listaDeContraseñasPuntuadas:
            archivo.write(f"Contraseña: {password} | Puntuacion: {puntuacion} | Categoria: {categoria}\n")

# Programa principal 
lineasPass = leer_archivo("Contraseñas - Proyecto (Fundamentos de Programación).txt")
lineasOdvios = leer_archivo("Patrones obvios de contraseña - Proyecto (Fundamentos de Programación).txt")

minusculas = 'abcdefghijklmnopqrstuvwxyz'
mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '1234567890'

listaDeContraseñasPuntuadas = []

for password in lineasPass:
    password = password.strip()  # Quitar salto de línea al principio y al final de la contraseña

    puntuacion = calcular_puntaje(password, lineasOdvios, minusculas, mayusculas, numeros)
    categoria = clasificar_contraseña(puntuacion)
    listaDeContraseñasPuntuadas.append((password, puntuacion, categoria))

listaDeContraseñasPuntuadas = ordenar_contraseñas(listaDeContraseñasPuntuadas)
exportar_archivo("contraseñasClasificadas.txt", listaDeContraseñasPuntuadas)
