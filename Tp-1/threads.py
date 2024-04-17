from time import time
import numpy as np
from threading import Thread

def sum_elements(arr, results, i):
  for e in arr:
    results[i] += e

if __name__ == '__main__':
  n = 8  # Número de Threads
  c = 1000000  # Complejidad

  arr = np.random.rand(c)
  arr_splits = np.array_split(arr, n)  # Dividir el arreglo en n partes

  results = np.zeros(n)  # Inicializar un arreglo de resultados

  threads = [Thread(target=sum_elements, args=(arr_splits[i], results, i)) for i in range(n)] # target = def a ejecutar, args = parámetros a enviar a la función

  init = time()
  
  for thread in threads:
      thread.start()

  for thread in threads:
      thread.join()

  result = np.sum(results)  # Suma de los resultados de cada hilo

  end = time() - init

  print("Result:", result, "Time:", end, "With C =", c, "With N = ",  n)