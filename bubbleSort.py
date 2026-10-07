def bubble_sort(vet):

    for i in range(len(vet), 1, -1):

        for j in range(0, i - 1):

            if vet[j] > vet[j + 1]:

                aux = vet[j]
                vet[j] = vet[j + 1]
                vet[j + 1] = aux