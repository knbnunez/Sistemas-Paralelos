from time import time
import numpy as np
from multiprocessing import Process

def sum_elements(arr, results, i):
  for e in arr:
    results[i] += e

if __name__ == '__main__':
  n = 16  # Número de Threads
  c = 100000000  # Complejidad

  arr = np.random.rand(c)
  arr_splits = np.array_split(arr, n)  # Dividir el arreglo en n partes

  results = np.zeros(n)  # Inicializar un arreglo de resultados

  processes = [Process(target=sum_elements, args=(arr_splits[i], results, i)) for i in range(n)] # target = def a ejecutar, args = parámetros a enviar a la función

  init = time()
  
  for process in processes:
      process.start()

  for process in processes:
      process.join()

  result = np.sum(results)  # Suma de los resultados de cada hilo

  end = time() - init

  print("Result:", result, "Time:", end, "With C =", c, "With N =", n)