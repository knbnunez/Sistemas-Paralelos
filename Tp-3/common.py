# Función que cada hilo ejecutará para calcular un segmento de la matriz resultante
def multiply_segment(A, B_T, result, start, end):
    num_cols_B = len(B_T)
    for index in range(start, end):
        row = index // num_cols_B
        col = index % num_cols_B
        sum_product = 0
        for k in range(len(B_T[0])):
            sum_product += A[row][k] * B_T[col][k]
        result[row][col] = sum_product


# Función para imprimir una matriz
def print_matrix(mat):
    for row in mat:
        print(" ".join(map(str, row)))


# Prepara los argumentos para los workers basados en el conteo de workers_counts
def prepare_arguments(A, B, workers_counts):
    num_rows_A = len(A)
    num_cols_B = len(B[0]) # Tomamos el largo del primer elemento porque intuímos que todas las filas tienen la misma cantidad de columnas...
    num_elements = num_rows_A * num_cols_B # Esta es la cantidad de elementos que tendrá la matriz resultante
    
    workers_args_list = []
    for count in workers_counts: # Recorremos el arreglo de cantidad de workers 
        workers_args = []
        
        if num_elements < count: # Caso existen menos elementos para calcular que workers
            # Asigna un elemento a cada uno de los primeros 'num_elements' workers
            for i in range(num_elements):
                workers_args.append((i, i+1))
            # Los workers restantes no hacen nada
            workers_args += [(i, i) for i in range(num_elements, count)]
        
        else:
            elements_per_thread = num_elements // count # La cantidad de elementos (celdas) que calculará de la matriz cada hilo
            extra = num_elements % count # Para que no queden elementos rezagados
            start = 0

            for i in range(count):
                end = start + elements_per_thread + (1 if i < extra else 0) # Asignación de la última fila a leer para el worker (i)
                workers_args.append((start, end)) # rango de elementos (celdas) efectivas a calcular por el worker (i)
                start = end

        workers_args_list.append(workers_args)
    return workers_args_list