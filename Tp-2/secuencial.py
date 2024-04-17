from time import time 
from common import *

if __name__ == '__main__':
    np = [1] # Secuencial
    #
    csv_list = leer_csv() # Conjunto de filas completo
    n_rows = len(csv_list)
    # 
    print("Begin: Secuencial")
    #
    for n in np:
        rowset = dividir_csv(csv_list, n_rows, n)
        #
        init = time()
        #
        calcular_imc(rowset[0])
        escribir_csv(rowset[0])
        #
        end = time() - init
        #
        print("Con n =",  n, "Tiempo final:", end)
    #
    print("End")