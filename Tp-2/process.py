from time import time 
from common import *
from multiprocessing import Process

def calcular_imc_y_escribir_csv(rows):
    calcular_imc(rows)
    escribir_csv(rows)

if __name__ == '__main__':
    np = [1, 2, 4, 8, 16]
    # 
    csv_list = leer_csv() 
    n_rows = len(csv_list)
    #
    print("Begin: Process")
    #
    for n in np:
        rowset = dividir_csv(csv_list, n_rows, n)
        #
        init = time()
        #
        processes = [Process(target=calcular_imc_y_escribir_csv, args=(rowset[i],)) for i in range(n)]
        for process in processes: process.start()
        for process in processes: process.join()
        #
        end = time() - init
        #
        print("Con n =",  n, "Tiempo final:", end)
    #
    print("End")