def run():
    secuencia = input('ingrese una secuencia de numeros: ')

    listado_secuencia = secuencia.split(',')

    for listado_secuencia in listado_secuencia:
        print(listado_secuencia)


if __name__ == '__main__':
    run()