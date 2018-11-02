import time
import random

my_randoms = random.sample(range(1000), 100)


def print_tab(tab, tab_length):
    for i in range (0, tab_length):
        print(tab[i], end='')
        if i < tab_length - 1:
            print(',', end='')
    print()


def min_tab(tab, tab_length):

    min = tab[0]
    for i in range(1, tab_length):
        if tab[i] < min:
            min = tab[i]
    return min


def max_tab(tab, tab_length):
    max = tab[0]
    for i in range(1, tab_length):
        if tab[i] > max:
            max = tab[i]
    return max


def index_min_tab(tab, tab_length):
    min = tab[0]
    index_min = 0
    for i in range(1, tab_length):
        if tab[i] < min:
            min = tab[i]
            index_min = i
    return index_min


def select_sort_tab(tab, tab_length):
    start_time = time.time()
    print('--début du tri sélection--')
    for j in range(0, tab_length):
        min = tab[j]
        index_min = j
        for i in range(j+1, tab_length):
            if tab[i] < min:
                min = tab[i]
                index_min = i
        tmp = tab[j]
        tab[j] = tab[index_min]
        tab[index_min] = tmp
        print_tab(tab, tab_length)
    print('--fin du tri sélection--')
    print("Execution time : %s seconds" % (time.time() - start_time))


def bubble_sort_tab(tab, table_length):
    start_time = time.time()
    swap = 1
    print('--debut du tri à bulle--')
    print_tab(tab, table_length)
    while swap == 1:
        print_tab(tab, table_length)
        swap = 0
        for i in range(0, table_length-1):
            if tab[i] > tab[i+1]:
                tmp = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = tmp
                swap = 1
    print('--fin du tri à bulle--')
    print("Execution time : %s seconds" % (time.time() - start_time))


# for i in range(0, 10):
#     saisie = int(input('Saisir un entier'))
#     tab.append(saisie)

tab = [37, 10, 8, 29, 97, 4, 11, 76, 55, 34]

select_tab = list(tab)
bubble_tab = list(tab)

print('Affichage du tableau: ', end='')
print_tab(tab, len(tab))
print('Fonction min: ', min_tab(tab, len(tab)))
print('Fonction indicemin: ', index_min_tab(tab, len(tab)))

select_sort_tab(select_tab, len(select_tab))
print('Affichage du tableau après tri: ', end='')
print_tab(select_tab, len(select_tab))

bubble_sort_tab(bubble_tab, len(bubble_tab))
print('Affichage du tableau après tri: ', end='')
print_tab(bubble_tab, len(bubble_tab))

