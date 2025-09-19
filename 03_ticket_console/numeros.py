def decorar_turno(gen):

    def mostrar_turno():
        print("Su turno es: ")
        print(next(gen))
        print("Aguarde y será atendido")
    return mostrar_turno


def perfumeria():
    num = 1
    while True:
        yield "P-" + str(num)
        num += 1


def farmacia():
    num = 1
    while True:
        yield "F-" + str(num)
        num += 1


def cosmeticos():
    num = 1
    while True:
        yield "C-" + str(num)
        num += 1
