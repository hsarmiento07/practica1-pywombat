def last_elements(lista, cantidad):
    return tuple(lista[-cantidad:])


def run():
    mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    valor = last_elements(mi_lista, 2)
    print(valor)


if __name__ == '__main__':
    run()