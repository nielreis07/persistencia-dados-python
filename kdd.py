import time

def bubble_sort(arr):
    array = arr.copy()
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def selection_sort(arr):
    array = arr.copy()
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

with open("loremipsum.txt", "r") as f:
    palavras = []
    for linha in f:
        palavras.extend(linha.split())

inicio = time.time()
b1 = bubble_sort(palavras)
fim = time.time()
print("Bubble:", fim - inicio)

inicio = time.time()
s1 = selection_sort(palavras)
fim = time.time()
print("Selection:", fim - inicio)

inicio = time.time()
n1 = sorted(palavras)
fim = time.time()
print("Sort nativo:", fim - inicio)

# Escolhido: sort nativo
with open("resultado.txt", "w") as f:
    for palavra in n1:
        f.write(palavra + "\n")
