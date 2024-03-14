# Password Generator Project
import random

def password_create():
    # Definición de listas de caracteres
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']




    #se escoge aleatoriamente el numero de letras, simbolos y numeros que nuestra password tendra
    nr_letters = random.randint(8,10)

    nr_symbols = random.randint(2,4)

    nr_numbers = random.randint(2,4)

    # Lista para almacenar el resultado final de la contraseña
    password = []

    # Generar letras aleatorias de la lista 'letters' y agregarlas a la lista de contraseñas, el ciclo for se repite segun el 'nr_letters'
    password=[ random.choice(letters) for i in range(nr_letters)]
    
    # Generar símbolos aleatorios y agregarlos a la lista de contraseñas
    for i in range(0, nr_symbols):
        random_number_symbol = random.randint(0, len(symbols)-1)
        password.append(symbols[random_number_symbol])

    # Generar números aleatorios y agregarlos a la lista de contraseñas
    for i in range(0, nr_numbers):
        random_number_numbers = random.randint(0, len(numbers)-1)
        password.append(numbers[random_number_numbers])

    # usamos la funcion shuffle para mezclar nuestra lista
    random.shuffle(password)

    # Convertir la lista de contraseñas en una cadena
    password_string = ''.join(password)

    # Imprimir la contraseña generada
    return password_string


