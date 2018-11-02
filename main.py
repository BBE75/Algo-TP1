import time
import random




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


def index_min_tab(tab, tab_length):
    min = tab[0]
    index_min = 0
    for i in range(1, tab_length):
        if tab[i] < min:
            min = tab[i]
            index_min = i
    return index_min


def select_sort_tab(tab, tab_length, verbose):
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
        if verbose == 1:
            print_tab(tab, tab_length)
    print('--fin du tri sélection--')
    print("Execution time : %s seconds" % (time.time() - start_time))


def bubble_sort_tab(tab, table_length, verbose):
    start_time = time.time()
    swap = 1
    print('--debut du tri à bulle--')
    j = 1
    while swap == 1:
        if verbose == 1:
            print_tab(tab, table_length)
        swap = 0
        for i in range(0, table_length-j):
            if tab[i] > tab[i+1]:
                tmp = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = tmp
                swap = 1
        j += 1
    print('--fin du tri à bulle--')
    print("Execution time : %s seconds" % (time.time() - start_time))


# for i in range(0, 10):
#     saisie = int(input('Saisir un entier'))
#     tab.append(saisie)

tab = [37, 10, 8, 29, 97, 4, 11, 76, 55, 34]

select_tab = list(tab)
bubble_tab = list(tab)

print('--------------------------- 10 elements -----------------------------------------------------------------------')
print('Affichage du tableau: ', end='')
print_tab(tab, len(tab))
print('Fonction min: ', min_tab(tab, len(tab)))
print('Fonction indicemin: ', index_min_tab(tab, len(tab)))

select_sort_tab(select_tab, len(select_tab), 1)
print('Affichage du tableau après tri: ', end='')
print_tab(select_tab, len(select_tab))

bubble_sort_tab(bubble_tab, len(bubble_tab), 1)
print('Affichage du tableau après tri: ', end='')
print_tab(bubble_tab, len(bubble_tab))

print('--------------------------- Custom elements -------------------------------------------------------------------')
nb_values = int(input('Saisir le nombre d\'élèments voulues (max 999)'))
my_randoms = random.sample(range(1000), nb_values)
select_tab2 = list(my_randoms)
bubble_tab2 = list(my_randoms)
select_sort_tab(select_tab2, len(select_tab2), 0)
bubble_sort_tab(bubble_tab2, len(bubble_tab2), 0)
