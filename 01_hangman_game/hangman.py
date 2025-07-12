import random

my_list = ["apple", "banana", "cherry"]
palabra = random.choice(my_list)


estado = ["_" for _ in palabra]
vidas = 6
letras_usadas = []

while vidas > 0 and "_" in estado:
    print("\nPalabra:", " ".join(estado))
    print(f"Vidas restantes: {vidas}")
    print(f"Letras usadas: {', '.join(letras_usadas)}")
    
    letra = input("Ingresa una letra: ").lower()
    
    if letra in letras_usadas:
        print("Ya usaste esa letra, intenta con otra.")
        continue  # Vuelve al inicio del while sin descontar vida
    
    letras_usadas.append(letra)
    
    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                estado[i] = letra
        print("¡Bien hecho!")
    else:
        vidas -= 1
        print(f"La letra '{letra}' no está en la palabra.")
        
if "_" not in estado:
    print("\n¡Felicidades! Adivinaste la palabra:", palabra)
else:
    print("\nTe quedaste sin vidas. La palabra era:", palabra)
