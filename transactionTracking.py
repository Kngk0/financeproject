class transactionTracker: 

	def __init__(self):
		self.expenses = []
		self.incomes = []

	# Method to add expenses
	def addExpense(self, date, amount, category, payment, to, status,  description = ''):
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

# Method to view expenses
	def view(self):
		summary = {
 			"Total Expenses": 0,
 			"Total Income": 0
 		}
		
		totalExpenses = 0
		
		for expense in self.expenses:
			print(f'Date: {expense['Date']}')
			print(f'Amount: {expense['Amount']:,.2f}')
			print(f'Category: {expense['Category']}')
			print(f'Description: {expense['Description']}')
			print(f'Payment Mehod: {expense['Payment Method']}')
			print(f'Merchent: {expense['To']}')
			print(f'Payment Status: {expense['Payment Status']}')
			print()
			totalExpenses += expense["Amount"]
			
		summary["Total Expenses"] = f"${totalExpenses:,.2f}"
		
		# Initalize total income to zero
		totalIncome = 0
		
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
		
		print(summary)

	def search(self, searchTerm):
		found = False
		for expense in self.expenses:
			for value in expense.values():
				if searchTerm in str(value):
					print(f'Date: {expense["Date"]}')
					print(f'Amount: {expense["Amount"]:,.2f}')
					print(f'Category: {expense["Category"]}')
					print(f'Description: {expense["Description"]}')
					print(f'Payment Method: {expense["Payment Method"]}')
					print(f'To: {expense["To"]}')
					print(f'Payment Status: {expense["Payment Status"]}')
					print()
					found = True
					break
				
		for income in self.incomes:
			for value in income.values():
				if searchTerm in str(value):
					print(f'Date: {income["Date"]}')
					print(f'Amount: {income["Amount"]:,.2f}')
					print(f'Category: {income["Category"]}')
					print(f'Description: {income["Description"]}')
					print(f'Income Type: {income["Income Type"]}')
					print(f'Source: {income["Source"]}')
					print(f'Status: {income["Status"]}')
					print()
					found = True
					break

		if not found:
			print('No results for "' + searchTerm + '"')
			print('Check the spelling or try a new search.')
			print()