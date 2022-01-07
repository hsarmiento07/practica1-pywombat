def run():
    A = int(input('ingresa el valor de A: '))
    B = int(input('ingresa el valor de B: '))
    C = int(input('ingresa el valor de C: '))

    resultado = A + B + C
    total = (180)
    print(resultado)

    if resultado == total:
        print("es un trangulo")
    else:
        print("no es un triangulo")


if __name__ == '__main__':
    run()