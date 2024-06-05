import csv

# Task 1: Read the data from the spreadsheet
def read_data(file_path):
    data = []
    with open(file_path, 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data

# Task 2: Collect all of the sales from each month into a single list
def collect_sales(data):
    sales = []
    for row in data:
        sale = int(row['sales'])  # Assuming the column containing sales is named 'sales'
        sales.append(sale)
    return sales

# Task 3: Output the total sales across all months
def calculate_total_sales(sales):
    total = sum(sales)
    return total

def run():
    file_path = 'sales.csv'
    data = read_data(file_path)
    sales = collect_sales(data)
    total = calculate_total_sales(sales)
    print('Total sales: {}'.format(total))

run()
