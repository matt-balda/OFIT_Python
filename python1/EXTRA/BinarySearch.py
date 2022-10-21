from random import randint

def binarySearch(array, x, low, high):
    # Enquanto o low for menor ou igual ao high, segue repetindo
    while low <= high:

        mid = low + (high - low) // 2  # n numero de elementos no vetor, dividido por 2

        if array[mid] == x:  # se o elemento que busca, estiver diretamente no meio retorna ele
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


def main():
    x = int(input('Quantos elementos: '))
    vec = []

    for i in range(x):
        vec.append(randint(0, 300))

    vec.sort()  # ordenacao do vetor

    print(vec)

    y = int(input('Qual elemento busca? '))

    result = binarySearch(vec, y, 0, len(vec) - 1)

    if result != -1:
        print("Elemento presente " + str(result))
    else:
        print("Não procurado")

if __name__ == '__main__':

    main()
