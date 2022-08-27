# Generador de password seguro y  codigo abierto
# Desarollado por Goktug Erol
# ge_dev@yahoo.com

import string
import random

# Caracteres para generar la contraseña
letras = list(string.ascii_letters)
digits = list(string.digits)
special_char = list("!@#$%^&*()_-/?¿")
caracteres = list(string.ascii_letters + string.digits + "!@#$%^&*()_-/?¿")

def gen_rand_pas():

        # Longtitud de la contraseña
        length = int(input("Entra longtitud de la contraseña: "))

        # La cantidad de tipos de character
        letras_count = int(input("Entra cuantas letras tenga la contraseña: "))
        digits_count = int(input("Entra cuantos digitos tenga la contraseña: "))
        special_char_count = int(input("Entra cuantos caracteres especiales tenga la contraseña: "))

        characters_count = letras_count + digits_count + special_char_count

        # Checa longtitud total con caracteres sumidos
        # Print inválido si cantidad total es mayor que longtitud
        if characters_count > length:
            print("ERROR - La cantidad de caracteres ingresados es mayor que longtitud total de la contraseña")
            return


        # Iniziando la contraseña
        password = []

        # Eligiendo letras random
        for i in range(letras_count):
            password.append(random.choice(letras))

        # Eligiendo digitos random
        for i in range(digits_count):
            password.append(random.choice(digits))

        # Eligiendo random letras
        for i in range(special_char_count):
            password.append(random.choice(special_char))

        # Cuando char count es menos que tammaño de password
        # Agrega random caracteres para igualar longtitud
        if characters_count < length:
            random.shuffle(caracteres)
            for i in range(length - characters_count):
                password.append(random.choice(caracteres))


        # Mezclando passwd resultante
        random.shuffle(password)

        # Convirtiendo la lista a string
        # Printing la lista
        print("".join(password))

# Invoking la function
gen_rand_pas()
