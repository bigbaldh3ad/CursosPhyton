import random

def main():
    """Introduce el límite superior e inferior de un rango de números
    y permite al usuario adivinar el número aleatorio hasta acertar.
    """
    # Solicita al usuario que introduzca el número menor del rango
    limite_inferior = int(input("Introduce el número más pequeño del rango: "))
    # Solicita al usuario que introduzca el número mayor del rango
    limite_superior = int(input("Introduce el número más grande del rango: "))
    # Genera un número aleatorio entre los límites especificados
    numero_secreto = random.randint(limite_inferior, limite_superior)
    intentos = 0

    while True:
        # Incrementa el contador de intentos
        intentos += 1
        # Solicita al usuario que introduzca un número para intentar adivinar
        numero_usuario = int(input("Introduce un número para intentar adivinar: "))

        # Compara el número del usuario con el número secreto
        if numero_usuario < numero_secreto:
            print("Intenta con un número mayor.")
        elif numero_usuario > numero_secreto:
            print("Intenta con un número menor.")
        else:
            # Si el usuario acierta, se muestra un mensaje de éxito y se rompe el bucle
            print(f"¡Ganaste! Te tomó {intentos} intentos.")
            break

if __name__ == "__main__":
    main()
