import random
import time
import datetime
import sys

try:
    sys.setrecursionlimit(200000)
except (OverflowError, ValueError):
    print("No se pudo establecer un límite de recursión alto." "Merge Sort podría fallar en N=100000.")
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid] 
        R = arr[mid:]  
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bogo_sort(arr):
    def is_sorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

def format_time(seconds):
    return str(datetime.timedelta(seconds=seconds))

def main():
    options = {
        '1': 10,
        '2': 100,
        '3': 1000,
        '4': 10000,
        '5': 100000
    }
    print("Seleccione la cantidad de valores (N) para ordenar:")
    for key, value in options.items():
        print(f" {key}) {value} valores")
    choice = input("Ingrese su opción (1-5): ")
    if choice not in options:
        print("Opción no válida. Saliendo.")
        return
    N = options[choice]
    print(f"\nGenerando {N} valores aleatorios")
    original_list = [random.randint(0, N * 10) for _ in range(N)]
    results = {}

    print("Ejecutando Bubble Sort...")
    arr_copy = original_list.copy()
    start_time = time.perf_counter()
    bubble_sort(arr_copy)
    end_time = time.perf_counter()
    results['Bubble Sort'] = format_time(end_time - start_time)

    print("Ejecutando Merge Sort...")
    arr_copy = original_list.copy()
    start_time = time.perf_counter()
    merge_sort(arr_copy)
    end_time = time.perf_counter()
    results['Merge sort'] = format_time(end_time - start_time)

    print("Ejecutando Selection Sort...")
    arr_copy = original_list.copy()
    start_time = time.perf_counter()
    selection_sort(arr_copy)
    end_time = time.perf_counter()
    results['Selection'] = format_time(end_time - start_time)
    print("Ejecutando Bogo Sort...")
    if N > 11: 
        results['Bogo Sort'] = "(Se te quema la PC)"
    else:
        arr_copy = original_list.copy()
        start_time = time.perf_counter()
        bogo_sort(arr_copy)
        end_time = time.perf_counter()
        results['Bogo Sort'] = format_time(end_time - start_time)
    print("\n" + "="*115)
    print("Resultados de Tiempos de Ejecución")
    print("="*115)
    print(f"{'N':<10} | {'Bubble Sort':<25} | {'Merge sort':<25} | {'Selection':<25} | {'Bogo Sort (Stupid sort)':<25}")
    print("-" * 115) 
    row = (f"{N:<10} | "
           f"{results.get('Bubble Sort', 'Error'):<25} | "
           f"{results.get('Merge sort', 'Error'):<25} | "
           f"{results.get('Selection', 'Error'):<25} | "
           f"{results.get('Bogo Sort', 'Error'):<25}")
    print(row)
    print("\nEl tiempo es Hora:Minutos:Segundos.microsegundos")
if __name__ == "__main__":
    main()