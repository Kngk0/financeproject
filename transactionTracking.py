import datetime

class transactionTracker: 

	def __init__(self):
		self.expenses = []
		self.incomes = []

	# Method to add expenses
	def addExpense(self, date, amount, category, payment, to, status,  description = ''):
		if isinstance(date, datetime.date): # Ensure it's a date object before formatting
			date = date.strftime('%Y-%m-%d') # Convert to 'YYYY-MM-DD' format
			
		expense = {
 			"Date": date,
 			"Amount": amount,
 			"Category": category,
 			"Description": description,
 			"Payment Method": payment,
 			"To": to,
 			"Payment Status": status
		}
		
		self.expenses.append(expense)
		for key, value in expense.items():
			if key == 'Amount':
				print(f'{key}: ${value:,.2f}')
			else:
				print(f'{key}: {value}')
				 
	# Method to add income
	def addIncome(self, date, amount, category, incomeType, source, status, description = ''):
		# DEFINE income AS DICTIONARY OF DATE, AMOUNT, CATEGORY, DESCRIPTION, INCOME TYPE, SOURCE, STATUS
		if isinstance(date, datetime.date): # Ensure it's a date object before formatting
			date = date.strftime('%Y-%m-%d') # Convert to 'YYYY-MM-DD' format

		income = {
 			"Date": date,
 			"Amount": amount,
 			"Category": category,
 			"Description": description,
 			"Income Type": incomeType,
 			"Source": source,
 			"Status": status
 		}
		 
		self.incomes.append(income)
		for key, value in income.items():
			if key == "Amount":
				print(f'{key}: ${value:,.2f}')
			else:
				print(f'{key}: {value}')

# Method to view expenses and income
	def view(self):
		summary = {
 			"Total Expenses": 0,
 			"Total Income": 0
 		}
		
		totalExpenses = 0
		
		print("===== EXPENSES =====")
		for expense in self.expenses:
			print(f'Date: {expense['Date']}')
			print(f'Amount: {expense['Amount']:,.2f}')
			print(f'Category: {expense['Category']}')
			print(f'Description: {expense['Description']}')
			print(f'Payment Method: {expense['Payment Method']}')
			print(f'To: {expense['To']}')
			print(f'Payment Status: {expense['Payment Status']}')
			print()
			totalExpenses += expense["Amount"]
			
		summary["Total Expenses"] = f"${totalExpenses:,.2f}"
		
		# Initalize total income to zero
		totalIncome = 0
		
		print("===== INCOME =====")
		# Print income entries and calculate total income
		for income in self.incomes:
			print(f'Date: {income['Date']}')
			print(f'Amount: {income['Amount']:,.2f}')
			print(f'Category: {income['Category']}')
			print(f'Description: {income['Description']}')
			print(f'Income Type: {income['Income Type']}')
			print(f'Source: {income['Source']}')
			print(f'Status: {income['Status']}')
			print()
			totalIncome += income["Amount"]

		summary['Total Income'] = f"${totalIncome:,.2f}"
		
		print("===== SUMMARY =====")
		print(summary)
		print()

	def search(self, searchTerm):
		found = False
		
		print(f'Search results for "{searchTerm}":\n')
		
		for expense in self.expenses:
			if any(searchTerm in str(value) for value in expense.values()):
				print(f'Date: {expense["Date"]}')
				print(f'Amount: {expense["Amount"]:,.2f}')
				print(f'Category: {expense["Category"]}')
				print(f'Description: {expense["Description"]}')
				print(f'Payment Method: {expense["Payment Method"]}')
				print(f'To: {expense["To"]}')
				print(f'Payment Status: {expense["Payment Status"]}')
				print()
				found = True
				
		for income in self.incomes:
			if all(searchTerm in str(value) for value in income.values()):
				print(f'Date: {income["Date"]}')
				print(f'Amount: {income["Amount"]:,.2f}')
				print(f'Category: {income["Category"]}')
				print(f'Description: {income["Description"]}')
				print(f'Income Type: {income["Income Type"]}')
				print(f'Source: {income["Source"]}')
				print(f'Status: {income["Status"]}')
				print()
				found = True

		if not found:
			print(f'No results found for "{searchTerm}".')
			print('Check the spelling or try a new search.\n')