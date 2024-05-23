# Inputting, categorizing, saving, and controlling expenses.
# 1. Users should be able to input their daily expenses, including the amount and category (e.g., groceries, utilities, entertainment).
class expensetracker: 

 	def __init__(self):
 		self.expenses = {
 			'Date': [],
 			'Amount': [], 
 			'Category': [], 
 			'Description': [],
 			'Payment Method': [],
 			'To': [],
 			'Payment Status': [],
 		}

# 2. The application should allow users to add, remove, and update expenses.
 	def add(self, date, amount, category, payment, to, status,  description = ' '):
 		self.expenses['Date'].append(date)
 		self.expenses['Amount'].append(amount)
 		self.expenses['Category'].append(category)
 		self.expenses['Description'].append(description)
 		self.expenses['Payment Method'].append(payment)
 		self.expenses['To'].append(to)
 		self.expenses['Payment Status'].append(status)
 		newExpense = {
 			'Date': date,
 			'Amount': amount,
 			'Category': category,
 			'Description': description,
 			'Payment Method': payment,
 			'To': to,
 			'Payment Status': status
 		}
 		for x, y in newExpense.items():
 			print(x, ':', y)


# 3. Users should be able to view a summary of their expenses, categorized by expense type, and the total spending.