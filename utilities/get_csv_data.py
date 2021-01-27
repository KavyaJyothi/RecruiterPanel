import  csv

def read_csv_data(file_name):
    rows=[]
    with open(file_name, 'r') as data1:
        reader=csv.reader(data1)
        next(reader)
        for row in reader:
            rows.append(row)

    return rows

