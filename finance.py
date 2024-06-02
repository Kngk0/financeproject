# user-friendly menu interface
import expensetracking
import datetime
# 1. The application should feature a command-line interface that is intuitive and easy to navigate.
# 2. Users should be able to interact with the application through text-based commands and receive informative prompts and messages
def main_menu():
	while True:
		print('==============================')
		print('Main Menu')
		print('==============================')
		print('1. Track Expenses')
		print('2. Manage Budget')
		print('3. Calculator')
		print('4. Exit\n')
		choice = input('Enter your choice (1-4: ')
		print()
		if choice.strip():
			if choice == '1':
				track = expensetracking.expensetracker()
				while True:
	 				print('==============================')
	 				print('Expense Tracker Menu')
	 				print('==============================')
	 				print('1. Add Expense')
	 				print('2. View Expenses')
	 				print('3. Delete Expense')
	 				print('4. Search Expense')
	 				print('5. Generate Report')
	 				print('6. Back\n')
	 				choice = input('Enter your choice (1-7): ')
	 				print()
	 				if choice == '1':
	 					print('Please enter details of a new expense.')
	 					while True:
	 						date = input('Enter the date of the expense (YYYY-MM-DD): ').strip()
	 						try:
	 							datetime.datetime.strptime(date, '%Y-%m-%d')
	 							break
	 						except ValueError:
	 							print('Invalid date format. Please enter the date in the format YYYY-MM-DD.')
	 					while True:
	 						amount = input('Enter the amount spent: $').strip()
	 						try:
	 							amount = float(amount)
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
	 					method = ['cash', 'credit card', 'debit card', 'bank transfer', 'check)']
	 					while True:
	 						payment = input('Specify the payment method (Cash, Credit Card, Debit Card, Bank Transfer, Check: ').strip().lower()
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
	 					newExpense = track.add(date, amount, category, payment, to, status, description)
	 					print('\n')
	 				elif choice == '2':
	 					viewExpense = track.view()
	 					while True:
	 						edit = input('Enter the number of the expense to edit, "d" to delete an expense, or "b" to go back: ')
	 						length = len(next(iter(track.expenses.values())))
	 						if edit.isdigit() and 1 <= int(edit) <= length:
	 							pass
	 						elif edit == 'd':
	 							pass
	 						elif edit == 'b':
	 							break
	 						else:
	 							print('Invalid input, please try again.')
	 				elif choice == '3':
	 					print('You selected Delete expense')
	 				elif choice == '4':
	 					print('You selected Search expense')
	 				elif choice == '5':
	 					print('You selected Generate Report')
	 				elif choice == '6':
	 					print('You selected back')
	 					break
			elif choice == '2':
				print('You selected Manage Budget')
			elif choice == '3':
				print('You selected Calculator')
			elif choice == '4':
				print('Exiting program. Goodbye!')
				break
		else:
			print('Invalid choice. Please select a number from the menu')


main_menu()