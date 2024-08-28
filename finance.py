# user-friendly menu interface
import expensetracking
import budgetmanagement
import datetime
# 1. The application should feature a command-line interface that is intuitive and easy to navigate.
# 2. Users should be able to interact with the application through text-based commands and receive informative prompts and messages
def main_menu():
	track = expensetracking.expensetracker()
	budget = budgetmanagement.management()
	while True:
		print('==============================')
		print('Main Menu')
		print('==============================')
		print('1. Track Expenses')
		print('2. Manage Budget')
		print('3. Calculator')
		print('4. Exit\n')
		choice = input('Enter your choice (1-4): ')
		print()
		if choice.strip():
			if choice == '1':
				while True:
	 				print('==============================')
	 				print('Expense Tracker Menu')
	 				print('==============================')
	 				print('1. Add Expense')
	 				print('2. View Expenses')
	 				print('3. Search Expense')
	 				print('4. Back\n')
	 				choice = input('Enter your choice (1-4): ')
	 				print()
	 				if choice == '1':
	 					print('Please enter details of a new expense.')
	 					while True:
	 						date = input('Enter the date of the expense (YYYY-MM-DD): ').strip()
	 						if not date:
	 							print('Please enter the date for this expense.')
	 							continue
	 						try:
	 							date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
	 							if date <= datetime.datetime.today().date():
	 								break
	 							else:
	 								print('The date cannot be in the future. Please enter a valid date.')
	 						except ValueError:
	 							print('Invalid date format. Please enter the date in the format YYYY-MM-DD.')
	 					while True:
	 						amount = input('Enter the amount spent: $').strip()
	 						if not amount:
	 							print('Please enter the amount for this expense.')
	 							continue
	 						try:
	 							amount = float(amount.replace(',',''))
	 							if amount <= 0:
	 								print('Amount must be a positive number.')
	 							else:
	 								break
	 						except ValueError:
	 							print('Invalid amount. Please enter a valid number.')
	 					while True:
	 						category = input('Enter the category for this expense: ').strip()
	 						if not category:
	 							print('Please enter the category for this expense.')
	 						else:
	 							break
	 					description = input('Optionally, add a brief description for this expense:\n').strip()
	 					if description:
	 						pass
	 					else:
	 						print('No description provided for this expense.')
	 					method = ['cash', 'credit card', 'debit card', 'bank transfer', 'check']
	 					while True:
	 						payment = input('Specify the payment method (Cash, Credit Card, Debit Card, Bank Transfer, Check): ').strip().lower()
	 						if payment in method:
	 							break
	 						else:
	 							print('Please enter a valid payment method from the options provided.')
	 					while True:
	 						to = input('Enter the recipient: ').strip()
	 						if not to:
	 							print('Please enter the recipient of this expense.')
	 						else:
	 							break
	 					payment_status = ['paid', 'pending']
	 					while True:
	 						status = input('Paid or Pending?: ').strip().lower()
	 						if status in payment_status:
	 							break
	 						else:
	 							print('Please enter a valid payment status.')
	 					print('\nExpense added successfully:')
	 					track.add(date, amount, category, payment, to, status, description)
	 					print('\n')
	 				elif choice == '2':
	 					track.view()
	 					empty = True
	 					for items in track.expenses:
	 						if items:
	 							empty = False
	 							break
	 					if empty:
	 						print('No expenses to show.\n')
	 					else:
			 				while True:
			 					edit = input('Enter the number of the expense to edit, "d" to delete an expense, or "b" to go back: ')
			 					if edit.isdigit():
			 						index = int(edit) - 1
			 						length = len(track.expenses)
			 						# length = len(next(iter(track.expenses.values())))
			 						if 0 <= index < length:
			 							while True:
			 								newDate = input('Enter new date (YYYY-MM-DD) or press Enter to keep current: ').strip()
			 								if newDate:
			 									try:
			 										newDate = datetime.datetime.strptime(newDate, '%Y-%m-%d').date()
			 										if newDate <= datetime.datetime.today().date():
			 											break
			 										else:
			 												print('The date cannot be in the future. Please enter a valid date.')
			 									except ValueError:
			 										print('Invalid date format. Please enter the date in the format YYYY-MM-DD')
			 								else:
			 									break
			 							while True:
			 								newAmount = input('Enter new amount or press Enter to keep current: ').strip()
			 								if newAmount:
			 									try:
			 										newAmount = float(newAmount)
			 										if newAmount <= 0:
			 											print('Amount must be a positive number.')
			 										else:
			 											break
			 									except ValueError:
			 										print('Invalid amount. Please enter a valid number.')
			 								else:
			 									break
			 							newCategory = input('Enter new category or press Enter to keep current: ').strip()
			 							newDescription = input('Enter new description or press Enter to keep current: ').strip()
			 							while True:
			 								newPayment = input('Enter new payment method (Cash, Credit Card, Debit Card, Bank Transfer, Check) or press Enter to keep current: ').strip().lower()
			 								if newPayment:
			 									if newPayment in method:
			 										break
			 									else:
			 										print('Please enter a valid payment method from the options provided.')
			 								else:
			 									break
			 							newTo = input('Enter new recipient or press Enter to keep current: ').strip()
			 							while True:
			 								newStatus = input('Enter new payment status or press Enter to keep current: ').strip().lower()
			 								if newStatus:
			 									if newStatus in payment_status:
			 										pass  # Replace with code to handle the new status if needed
			 									else:
			 										print('Please enter a valid payment status.')
			 								else:
			 									break
			 							while True:
			 								save = input('Save changes? (yes/no): ').strip().lower()
			 								if save == 'yes':
			 									track.edit(index, newDate, newAmount, newCategory, newPayment, newTo, newStatus, newDescription)
			 									print('\nExpense updated successfully!\n')
			 									break
			 								elif save == 'no':
			 									break
			 								else:
			 									print('Please enter yes or no.')
			 						else:
			 							print('Invalid number. Please try again.')
			 					elif edit == 'd':
			 						delete = input('Enter the number of the expense to delete: ')
			 						if delete.isdigit():
			 							index = int(delete) - 1
			 							length = len(track.expenses)
			 							#length = len(next(iter(track.expenses.values())))
			 							if 0 <= index < length:
			 								while True:
			 									confirm = input(f'Are you sure you would like to delete expense {index + 1}? (yes/no): ').strip().lower()
			 									if confirm == 'yes':
			 										track.delete(index)
			 										print('\nExpense deleted successfully!\n')
			 										empty = True
			 										for items in track.expenses:
			 											if items:
			 												empty = False
			 												break
			 										if empty:
			 											print('No expenses to show.\n')
			 											break
			 										else:
			 											break
			 									elif confirm == 'no':
			 										print()
			 										break
			 									else:
			 										print('Please enter yes or no.')
			 							else:
			 								print('Invalid number. Please try again.')
			 					elif edit == 'b':
			 						break
			 					else:
			 						print('Invalid input, please try again.')
	 				elif choice == '3':
	 					while True:
	 						search = input('Search (or type "exit" to quit): ')
	 						if search.lower() == 'exit':
	 							break
	 						track.search(search)
	 				elif choice == '4':
	 					print('You selected back')
	 					break
	 				else:
	 					print('Please enter a valid choice (1-4)\n')
			elif choice == '2':
				print('You selected Manage Budget')
				while True:
					print('==============================')
					print('Budget Management Menu')
					print('==============================')
					print('1. Add Income')
					print('2. Set or Update Budget')
					print('3. View Budget')
					print('4. Back\n')
					choice = input('Enter your choice (1-4): ')
					print()
					if choice == '1':
						print('Please enter details of a new income.')
						while True:
							date = input('Enter the date of the income (YYYY-MM-DD): ').strip()
							if not date:
								print('Please enter the date for this income.')
								continue
							try:
								date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
								break
							except ValueError:
								print('Invalid date format. Please enter the date in the format YYYY-MM-DD.')
						if date > datetime.datetime.today().date():
							status = 'pending'
						else:
							status = 'paid'
						while True:
							amount = input('Enter the amount of income: $').strip()
							if not amount:
								print('Please enter the amount for this expense.')
								continue
							try:
								amount = float(amount.replace(',',''))
								if amount <= 0:
									print('Amount must be a positive number.')
								else:
									break
							except ValueError:
								print('Invalid amount. Please enter a valid number.')
						while True:
							category = input('Enter the category for this income: ').strip()
							if not category:
								print('Please enter the category for this income.')
							else:
								break
						description = input('Optionally, add a brief description for this income:\n').strip()
						if description:
							pass
						else:
							print('No description provided for this income.')
						incomeType = ['cash', 'credit', 'bank transfer', 'check']
						while True:
							type = input('Specify the income method (Cash, Credit, Bank Transfer, Check): ').strip().lower()
							if type in incomeType:
								break
							else:
								print('Please enter a valid income method from the options provided.')
						while True:
							source = input('Enter the source: ').strip()
							if not source:
								print('Please enter the source of this income.')
							else:
								break
						print('\nIncome added successfully:')
						budget.add(date, amount, category, type, source, status, description)
					elif choice == '2':
						print('You selected Set or Update Budget')
						print('Please enter details for budget')
						while True:
							category = input('Enter the budget category: ')
							if not category:
								print('Please enter the category for this budget.')
							else:
								break
						while True:
							budgetAmount = input("Enter the budget amount: $")
							if not budgetAmount:
								print('Please enter the amount for this budget')
								continue
							try:
								budgetAmount = float(budgetAmount.replace(',',''))
								if budgetAmount <= 0:
									print('Amount must be a positive number.')
								else:
									break
							except ValueError:
								print('Invalid amount. Please enter a valid number.')
						description = input("Enter a description for the budget (optional): ")
						if not description:
							print('No description provided for this budget.')
						print('\nBudget set successfully:')
						budget.setBudget(category, budgetAmount, description)
						print()
					elif choice == '3':
						print('You selected View Budget')
						
					elif choice == '4':
						break
					else:
						print('Please enter a valid choice (1-4)\n')
			elif choice == '3':
				print('You selected Calculator')
			elif choice == '4':
				print('Exiting program. Goodbye!')
				break
		else:
			print('Invalid choice. Please select a number from the menu')


main_menu()