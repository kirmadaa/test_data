from faker import Faker
import random
from datetime import datetime, timedelta
import csv

# Create a Faker instance
fake = Faker()

# Generate customers table
def generate_customers(num_customers):
    customers = []
    for _ in range(num_customers):
        customer_id = fake.unique.random_number(digits=6)
        name = fake.name()
        email = fake.email()
        address = fake.address()
        phone_number = fake.phone_number()
        customers.append(('customer_id', 'name', 'email', 'address', 'phone_number'))
    return customers

# Generate accounts table
def generate_accounts(num_accounts, customers):
    account_types = ['Savings', 'Checking', 'Credit Card']
    accounts = []
    used_ids = set()
    while len(accounts) < num_accounts:
        account_id = None
        while not account_id or account_id in used_ids:
            account_id = fake.random_number(digits=8)
        used_ids.add(account_id)
        customer_id = random.choice(customers)[0]
        account_type = random.choice(account_types)
        balance = fake.pydecimal(left_digits=6, right_digits=2, positive=True)
        opened_date = fake.date_between(start_date='-5y', end_date='today')
        accounts.append(('account_id', 'customer_id', 'account_type', 'balance', 'opened_date'))
    return accounts

# Generate transactions table
def generate_transactions(num_transactions, accounts):
    transaction_types = ['Deposit', 'Withdrawal', 'Transfer', 'Payment']
    transactions = []
    used_ids = set()
    while len(transactions) < num_transactions:
        transaction_id = None
        while not transaction_id or transaction_id in used_ids:
            transaction_id = fake.random_number(digits=6)
        used_ids.add(transaction_id)
        account_id = random.choice(accounts)[0]
        transaction_type = random.choice(transaction_types)
        amount = fake.pydecimal(left_digits=4, right_digits=2, positive=True)
        transaction_date = fake.date_time_between(start_date='-1y', end_date='now')
        transactions.append(('transaction_id', 'account_id', 'transaction_type', 'amount', 'transaction_date'))
    return transactions

# Generate branches table
def generate_branches(num_branches):
    branches = []
    for _ in range(num_branches):
        branch_id = fake.unique.random_number(digits=4)
        name = fake.company()
        address = fake.address()
        phone_number = fake.phone_number()
        branches.append(('branch_id', 'name', 'address', 'phone_number'))
    return branches

# Generate employees table
def generate_employees(num_employees, branches):
    job_titles = ['Manager', 'Teller', 'Loan Officer']
    employees = []
    for _ in range(num_employees):
        employee_id = fake.unique.random_number(digits=5)
        branch_id = random.choice(branches)[0]
        name = fake.name()
        job_title = random.choice(job_titles)
        email = fake.email()
        phone_number = fake.phone_number()
        employees.append(('employee_id', 'branch_id', 'name', 'job_title', 'email', 'phone_number'))
    return employees

# Generate loans table
def generate_loans(num_loans, customers):
    loans = []
    used_ids = set()
    while len(loans) < num_loans:
        loan_id = None
        while not loan_id or loan_id in used_ids:
            loan_id = fake.random_number(digits=6)
        used_ids.add(loan_id)
        customer_id = random.choice(customers)[0]
        amount = fake.pydecimal(left_digits=6, right_digits=2, positive=True)
        interest_rate = random.uniform(2, 8)
        start_date = fake.date_between(start_date='-2y', end_date='-1y')
        end_date = start_date + timedelta(days=random.randint(365, 1095))
        loans.append(('loan_id', 'customer_id', 'amount', 'interest_rate', 'start_date', 'end_date'))
    return loans

# Generate data
num_customers = 500000
num_accounts = 500000
num_transactions = 500000
num_branches = 10
num_employees = 5000
num_loans = 500000

# Generate customers table
print("Generating customers...")
customers = generate_customers(num_customers)
print("Customers generated:", len(customers))

# Generate accounts table
print("Generating accounts...")
accounts = generate_accounts(num_accounts, customers)
print("Accounts generated:", len(accounts))

# Generate transactions table
print("Generating transactions...")
transactions = generate_transactions(num_transactions, accounts)
print("Transactions generated:", len(transactions))

# Generate branches table
print("Generating branches...")
branches = generate_branches(num_branches)
print("Branches generated:", len(branches))

# Generate employees table
print("Generating employees...")
employees = generate_employees(num_employees, branches)
print("Employees generated:", len(employees))

# Generate loans table
print("Generating loans...")
loans = generate_loans(num_loans, customers)
print("Loans generated:", len(loans))

# Save data to CSV files
def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data[0])  # Write column names
        writer.writerows(data[1:])  # Write data rows

save_to_csv(customers, 'customers.csv')
save_to_csv(accounts, 'accounts.csv')
save_to_csv(transactions, 'transactions.csv')
save_to_csv(branches, 'branches.csv')
save_to_csv(employees, 'employees.csv')
save_to_csv(loans, 'loans.csv')

print("Data saved to CSV files.")
# hello

