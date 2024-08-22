# Inputting, categorizing, saving, and controlling expenses.
# 1. Users should be able to input their daily expenses, including the amount and category (e.g., groceries, utilities, entertainment).
class expensetracker: 

 	def __init__(self):
 		self.expenses = []#{
 			#'Date': [],
 			#'Amount': [], 
 			#'Category': [], 
 			#'Description': [],
 			#'Payment Method': [],
 			#'To': [],
 			#'Payment Status': [],
 		#}

	# Method to add expenses
 	def add(self, date, amount, category, payment, to, status,  description = ''):
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
 		for x, y in expense.items():
 			if x == 'Amount':
 				print(f'{x}: ${y:,.2f}')
 			else:
 				print(f'{x}: {y}')
 		#self.expenses['Date'].append(date)
 		#self.expenses['Amount'].append(amount)
 		#self.expenses['Category'].append(category)
 		#self.expenses['Description'].append(description)
 		#self.expenses['Payment Method'].append(payment)
 		#self.expenses['To'].append(to)
 		#self.expenses['Payment Status'].append(status)
 		#newExpense = {
 		#	'Date': date,
 		#	'Amount': amount,
 		#	'Category': category,
 		#	'Description': description,
 		#	'Payment Method': payment,
 		#	'To': to,
 		#	'Payment Status': status
 		#}
 		#for x, y in newExpense.items():
 			#if x == 'Amount':
 			#	print(f'{x}: ${y:,.2f}')
 			#else:
 			#	print(f'{x}: {y}')

 	# Method to view expenses
 	def view(self):
 		for expense in self.expenses:
 			print(f'Date: {expense['Date']}')
 			print(f'Amount: {expense['Amount']:,.2f}')
 			print(f'Category: {expense['Category']}')
 			print(f'Description: {expense['Description']}')
 			print(f'Payment Mehod: {expense['Payment Method']}')
 			print(f'Merchent: {expense['To']}')
 			print(f'Payment Status: {expense['Payment Status']}')
 			print()
 		#entries = len(self.expenses['Date'])
 		#for i in range(entries):
 		#	print(f'{i+1}:')
 		#	print(f'Date: {self.expenses["Date"][i]}')
 		#	print(f'Amount: ${self.expenses["Amount"][i]:,.2f}')
 		#	print(f'Category: {self.expenses["Category"][i]}')
 		#	print(f'Description: {self.expenses["Description"][i]}')
 		#	print(f'Payment Method: {self.expenses["Payment Method"][i]}')
 		#	print(f'To: {self.expenses["To"][i]}')
 		#	print(f'Payment Status: {self.expenses["Payment Status"][i]}')
 		#	print()


 	def edit(self, index, date = None, amount = None, category = None, payment = None, to = None, status = None, description = None):
 		if date:
 			self.expenses[index]['Date'] = date
 		if amount:
 			self.expenses[index]['Amount'] = amount
 		if category:
 			self.expenses[index]['Category'] = category
 		if description:
 			self.expenses[index]['Description'] = description
 		if payment:
 			self.expenses[index]['Payment Method'] = payment
 		if to:
 			self.expenses[index]['To'] = to
 		if status:
 			self.expenses[index]['Payment Status'] = status

 	def delete(self, index):
 		self.expenses.pop(index)

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
 					print(f'Merchant: {expense["To"]}')
 					print(f'Payment Status: {expense["Payment Status"]}')
 					print()
 					found = True
 					break
 		if not found:
 			print('No results for "' + searchTerm + '"')
 			print('Check the spelling or try a new search.')
 			print()
# 3. Users should be able to view a summary of their expenses, categorized by expense type, and the total spending.