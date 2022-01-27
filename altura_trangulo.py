def run():
    base = int(input('ingrese la base del triangulo: '))
    altura = int(input('ingrese la altura del triangulo: '))

    resultado = base * altura // 2
    print('El area del triangulo: ',resultado)


if __name__ == '__main__':
    run()