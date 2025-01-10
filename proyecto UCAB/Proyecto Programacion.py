passwords = open("passwords.txt", "r", encoding="utf-8")
lineasPass = passwords.readlines()
passwords.close()

patronesOdvios = open("patronesOdvios.txt", "r", encoding="utf-8")
lineasOdvios = patronesOdvios.readlines()
patronesOdvios.close()

minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

listaDeContraseñasPuntuadas = []

for password in lineasPass:
    if password[-1] == '\n':
        password = password[:-1]

    puntuacion = 0
    existeMinus = False
    existeMayus = False
    existeNums = False
    existeSimbols = False
    simbolosExtra = 0
    esPatronOdvio = False
    categoria = ""

    for i in range(len(password)):
        caracter = password[i]
        #no hacer lo demas cuando sea un salto de linea
        if caracter == '\n':
            continue
        #asignar la puntuacion     
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
    
    #revisar que no esten en patrones odvios
    for patrones in lineasOdvios:
        if patrones[-1] == '\n': #quitarle a los patrones los saltos de linea
            patrones = patrones[:-1]
        #ver si estan en patrones odvios y restarle puntos
        if password == patrones:
            esPatronOdvio = True
            puntuacion -= 5
            break
    #clasificar
    if puntuacion <= 15:
        categoria = "Debil"
    elif puntuacion > 15 and puntuacion <= 20:
        categoria = "Moderada"
    elif puntuacion > 20 and puntuacion <= 35:
        categoria = "Buena"
    elif puntuacion > 35 and puntuacion <= 100:
        categoria = "Excelente"
    elif puntuacion > 100:
        categoria = "Impenetrable"
    
    #añadir a la lista con sus 3 caracteristicas 
    listaDeContraseñasPuntuadas.append((password, puntuacion, categoria))

#ordenar en la lista
for i in range(len(listaDeContraseñasPuntuadas)):
    for j in range(0, len(listaDeContraseñasPuntuadas) - i - 1):
        if listaDeContraseñasPuntuadas[j][1] > listaDeContraseñasPuntuadas[j + 1][1]:
            listaDeContraseñasPuntuadas[j], listaDeContraseñasPuntuadas[j + 1] = listaDeContraseñasPuntuadas[j + 1], listaDeContraseñasPuntuadas[j]

#guardar en el archivo
with open("contraseñasClasificadas.txt", "w", encoding="utf-8") as guardarContraseñas:
    for password, puntuacion, categoria in listaDeContraseñasPuntuadas:
        guardarContraseñas.write(f"Contraseña: {password} | Puntuación: {puntuacion} | Categoria: {categoria} \n")


