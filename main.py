# Se requiere un programa para determinar cuál es el número más pequeño,
# cuál es el número más grande y cuál es el número intermedio de los tres ingresados.


if __name__ == '__main__':
    my_list = []
    swapped = True

    for i in range(3):
        val = float(input("Ingrese un número: "))
        my_list.append(val)

    while swapped:
        swapped = False
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                swapped = True
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

    print("\nEl número más grande es:", my_list[2])
    print("El número intermedio es:", my_list[1])
    print("El número más pequeño es:", my_list[0])
