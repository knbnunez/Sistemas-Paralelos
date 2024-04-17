import csv
# ............................................................................

def leer_csv():
    with open('data-imc.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        csv_list = []
        for row in reader: csv_list.append(row) 
        return csv_list

# ............................................................................

def dividir_csv(csv_list, n_rows, n):
    n_rowset = n_rows // n # División entera '//' operator
    rowset = []
    for i in range(n):
        start_idx = n_rowset * i
        end_idx = n_rowset * (i + 1)
        rows = []
        idx = start_idx
        while idx < end_idx: rows.append(csv_list[idx]); idx += 1
        rowset.append(rows)
    return rowset

# ............................................................................

def calcular_imc(rows):
    for row in rows:
        imc = round(int(row[1]) / ((int(row[2])/100) * (int(row[2])/100)), 2)
        row.append(imc) # Add al array

# ............................................................................

def escribir_csv(rows):
    with open('results-imc.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows: writer.writerow(row) # Escribe en el CSV