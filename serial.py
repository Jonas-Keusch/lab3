import csv

def load_data(filename):
    data = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({
                'date': row['date'],
                'profit_loss': float(row['profit_loss'])
            })
    return data

def search(data, target_date):
    for record in data:
        if record['date'] == target_date:
            return record['profit_loss']
    return None  

filename = 'budget_data.csv' 
financial_data = load_data(filename)

date = input("Input date you would like data for.")
result = search(financial_data, date)
