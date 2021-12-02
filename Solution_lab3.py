import numpy as np
from tabulate import *

lst = np.loadtxt("sol_lab3_input.txt", dtype='U', encoding='utf-8', delimiter=';')

kand_A = np.where(lst == 'А')
kand_A = list(kand_A[1])
kand_B = np.where(lst == 'Б')
kand_B = list(kand_B[1])
kand_C = np.where(lst == 'С')
kand_C = list(kand_C[1])

# Метод Кондорсе

A_1_1 = []
A_1_2 = []
B_1_1 = []
B_1_2 = []
C_1_1 = []
C_1_2 = []

for i in range(6):

    if kand_A[i] < kand_B[i]:
        A_1_1.append(int(lst[i][0]))
    if kand_B[i] < kand_A[i]:
        B_1_1.append(int(lst[i][0]))

    if kand_A[i] < kand_C[i]:
        A_1_2.append(int(lst[i][0]))
    if kand_C[i] < kand_A[i]:
        C_1_1.append(int(lst[i][0]))

    if kand_B[i] < kand_C[i]:
        B_1_2.append(int(lst[i][0]))
    if kand_C[i] < kand_B[i]:
        C_1_2.append(int(lst[i][0]))

suma_A_1_1 = sum(A_1_1)
suma_B_1_1 = sum(B_1_1)

suma_A_1_2 = sum(A_1_2)
suma_C_1_1 = sum(C_1_1)

suma_B_1_2 = sum(B_1_2)
suma_C_1_2 = sum(C_1_2)

sum_list_AB = [suma_A_1_1, suma_B_1_1]
sum_list_AB_max = max(sum_list_AB)
sum_list_AB_max_id = sum_list_AB.index(sum_list_AB_max)
if sum_list_AB_max_id == 0:
    result_AB_win = 'А'
if sum_list_AB_max_id == 1:
    result_AB_win = 'Б'

sum_list_AC = [suma_A_1_2, suma_C_1_1]
sum_list_AC_max = max(sum_list_AC)
sum_list_AC_max_id = sum_list_AC.index(sum_list_AC_max)
if sum_list_AC_max_id == 0:
    result_AC_win = 'А'
if sum_list_AC_max_id == 1:
    result_AC_win = 'С'

sum_list_BC = [suma_B_1_2, suma_C_1_2]
sum_list_BC_max = max(sum_list_BC)
sum_list_BC_max_id = sum_list_BC.index(sum_list_BC_max)
if sum_list_BC_max_id == 0:
    result_BC_win = 'Б'
if sum_list_BC_max_id == 1:
    result_BC_win = 'С'

k = [result_AB_win, result_AC_win, result_BC_win]
result_1 = max(set(k), key=k.count)

# Метод Борда

A_2 = []
B_2 = []
C_2 = []

for i in range(6):

    if kand_A[i] == 1:
        a = kand_A[i] + 1
    if kand_A[i] == 2:
        a = kand_A[i] - 1
    if kand_A[i] == 3:
        a = kand_A[i] - 3
    if kand_B[i] == 1:
        b = kand_B[i] + 1
    if kand_B[i] == 2:
        b = kand_B[i] - 1
    if kand_B[i] == 3:
        b = kand_B[i] - 3
    if kand_C[i] == 1:
        c = kand_C[i] + 1
    if kand_C[i] == 2:
        c = kand_C[i] - 1
    if kand_C[i] == 3:
        c = kand_C[i] - 3

    A_2.append(int(lst[i][0]) * a)
    B_2.append(int(lst[i][0]) * b)
    C_2.append(int(lst[i][0]) * c)

suma_A_2 = sum(A_2)
suma_B_2 = sum(B_2)
suma_C_2 = sum(C_2)

sum_list_2 = [suma_A_2, suma_B_2, suma_C_2]
sum_list_2_max = max(sum_list_2)
sum_list_2_max_id = sum_list_2.index(sum_list_2_max)
if sum_list_2_max_id == 0:
    result_2 = 'А'
if sum_list_2_max_id == 1:
    result_2 = 'Б'
if sum_list_2_max_id == 2:
    result_2 = 'С'

print("Вхідні дані:")
print(tabulate(headers=["Варіант", "Число виборців", "Переваги"],
               tabular_data=[[1, 34, "A > Б > С"], ['', 23, "А > С > Б"], ['', 26, "Б > А > С"], ['', 2, "Б > С > А"],
                             ['', 13, "С > А > Б"], ['', 12, "С > Б > А"]]))

print("Результат обрахунку:")
print(tabulate(headers=["Метод Кондорсе", "Метод Борда"], tabular_data=[[result_1, result_2]]))
