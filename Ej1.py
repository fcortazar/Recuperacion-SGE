import random # Importa la librería random

secret_number = random.randint(1, 100) # Crea un número aleatorio entre el 1 y el 100
intentos = 0 # Inicializa el contador de intentos

while intentos < 5: # Mientras el número de intentos sea menor a 5
    intento_actual = int(input("Adivina el número secreto entre 1 y 100: ")) # Pide un número al usuario
    intentos += 1 # Añade 1 el contador de intentos

    if intento_actual == secret_number: # Si el número es igual al número secreto
        print("¡Felicidades! Has adivinado el número secreto.") # Imprime un mensaje de felicitación
        break
    elif intento_actual < secret_number: # Si el número es menor al número secreto
        print("El número secreto es mayor que tu intento.") # Imprime un mensaje
    elif intento_actual > secret_number: # Si no, si el número es mayor al número secreto
        print("El número secreto es menor que tu intento.") # Si no, imprime otro mensaje
    else: # Si no, imprime otro mensaje
        print("Número no válido. Por favor, introduce un número entre 1 y 100.")

if intentos == 5 and intento_actual != secret_number: # Si el número de intentos es igual a 5 y el número no es igual al número secreto
    print("Lo siento, no has adivinado el número secreto. El número era", secret_number) # Imprime un mensaje con el número secreto
