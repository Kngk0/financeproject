# Inputting, categorizing, saving, and controlling expenses.

# 1. Users should be able to input their daily expenses, including the amount and category (e.g., groceries, utilities, entertainment).
class expensetracker: 

 	def __init__(self):
 		self.expenses = {
 							 'Date': [], 'Amount': [], 'Category': [], 
 							 'Description': [],'Payment Method': [], 'From': [],
 							 'Payment Status': [], 'Transaction ID': []
 							 }

 	def interface(self):
 		while True:
 			print('==============================')
 			print('Expense Tracker Menu')
 			print('==============================')
 			print('1. Add Expense')
 			print('2. View Expenses')
 			print('3. Edit Expense')
 			print('4. Delete Expense')
 			print('5. Search Expense')
 			print('6. Generate Report')
 			print('7. Back')
 			print('\n')
 			choice = input('Enter your choice (1-7): ')

 			if choice == '1':
 				print('You selected Add expense')
 			elif choice == '2':
 				print('You selected View expenses')
 			elif choice == '3':
 				print('You selected Edit expense')
 			elif choice == '4':
 				print('You selected Delete expense')
 			elif choice == '5':
 				print('You selected Search expense')
 			elif choice == '6':
 				print('You selected Generate Report')
 			elif choice == '7':
 				print('You selected back')
 				break


# 2. The application should allow users to add, remove, and update expenses.

# 3. Users should be able to view a summary of their expenses, categorized by expense type, and the total spending.