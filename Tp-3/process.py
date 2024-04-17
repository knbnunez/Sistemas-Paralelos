import random
from time import time
from common import *

from multiprocessing import Process


# Ejemplo de matrices A y B
# A = [
#     [1, 2],
#     [3, 4]
# ]

# B = [
#     [2, 0],
#     [1, 2]
# ]

# Matriz A de tamaño 100x50
A = [
    [random.randint(1, 10) for _ in range(50)]
    for _ in range(100)
]

# Matriz B de tamaño 50x100
B = [
    [random.randint(1, 10) for _ in range(100)]
    for _ in range(50)
]


# Arreglo con los conteos de trabajadores, workers (workers o procesos)
worker_counts = [1, 2, 4, 8, 16]
program_title = "Process"

if __name__ == "__main__":
    print(f"Begin: {program_title} \n")

    # Transpone la matriz B
    B_T = [[B[j][i] for j in range(len(B))] for i in range(len(B[0]))]
    
    # Prepara la lista de argumentos para los workers
    workers_args_list = prepare_arguments(A, B, worker_counts) # Retorna un arreglo de listas con los valores de argumento para cada uno de los workers en cada caso [[], [,], [,,,], ....]

    # Itera sobre la lista de conteos de workers y sus argumentos
    for count, worker_args in zip(worker_counts, workers_args_list): # A alto nivel ambos arreglos tienen la misma cantidad de elementos, luego internamente worker_counts tiene int's y workers_args_list otros arrays dentro
        result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]  # Inicializa la matriz resultante
        
        # Zona
        processes = [Process(target=multiply_segment, args=(A, B_T, result, *args)) for args in worker_args]
        #

        init = time()
        for process in processes:
            process.start()
        
        for process in processes:
            process.join()
        end = time() - init
        
        print("Con n =",  count, "Tiempo final:", end)
        # print_matrix(result)
    
    print("\nEnd...")