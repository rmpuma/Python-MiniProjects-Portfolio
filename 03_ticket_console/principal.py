import numeros


def main():
    # Crear generadores una sola vez
    gen_perfumeria = numeros.perfumeria()
    gen_farmacia = numeros.farmacia()
    gen_cosmeticos = numeros.cosmeticos()

    # Decorar una sola vez también
    turno_perfumeria = numeros.decorar_turno(gen_perfumeria)
    turno_farmacia = numeros.decorar_turno(gen_farmacia)
    turno_cosmeticos = numeros.decorar_turno(gen_cosmeticos)

    while True:
        print("\nHola, bienvenido a la farmacia Python")
        area = input("""¿A qué área te gustaría dirigirte?
1. Perfumería
2. Farmacia
3. Cosméticos
4. Salir
> """).lower()

        if area == "perfumeria":
            turno_perfumeria()
        elif area == "farmacia":
            turno_farmacia()
        elif area == "cosmeticos":
            turno_cosmeticos()
        elif area == "salir":
            print("¡Gracias por visitar la farmacia Python!")
            break
        else:
            print("Elige una opción válida.")


if __name__ == "__main__":
    main()
