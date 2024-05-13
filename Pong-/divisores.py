n = int(input("Ingrese num: "))


def divisores(num):
    cont = 0
    for x in range(2, num + 1):
        if num % x == 0:
            cont += 1

    return cont


print(f"La cantidad de divisores de '{n}' entre 2 y {n} son: {divisores(n)}")
