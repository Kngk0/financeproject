# user-friendly menu interface
import expensetracking
import datetime
# 1. The application should feature a command-line interface that is intuitive and easy to navigate.
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
		if choice.strip():
			if choice == '1':
				#print('You selected Track expenses')
				track = expensetracking.expensetracker()
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
	 				print('7. Back\n')
	 				choice = input('Enter your choice (1-7): ')

	 				if choice == '1':
	 					print('Please enter details of a new expense.')
	 					while True:
	 						date = input('Enter the date of the expense (YYYY-MM-DD): ')
	 						try:
	 							datetime.datetime.strptime(date, '%Y-%m-%d')
	 							break
	 						except ValueError:
	 							print('Invalid date format. Please enter the date in the format YYYY-MM-DD.')
	 					while True:
	 						amount = input('Enter the amount spent: $')
	 						try:
	 							amount = float(amount)
	 							if amount <= 0:
	 								print('Amount must be a positive number.')
	 							else:
	 								break
	 						except ValueError:
	 							print('Invalid amount. Please enter a valid number.')
	 					category = input('Enter the category for this expense: ')
	 					description = input('Optionally, add a brief description for this expense:\n')
	 					if description:
	 						continue
	 					else:
	 						print('No description provided for this expense.')
	 					method = ['cash', 'credit Card', 'debit Card', 'bank Transfer', 'check']
	 					while True:
	 						payment = input('Specify the payment method (Cash, Credit Card, Debit Card, Bank Transfer, Check: ').strip().lower()
	 						if payment in method:
	 							break
	 						else:
	 							print('Please enter a valid payment method from the options provided.')
	 					to = input('Enter the recipient: ')
	 					payment_status = ['paid', 'pending']
	 					while True:
	 						status = input('Paid or Pending: ').strip().lower()
	 						if status in payment_status:
	 							break
	 						else:
	 							print('Please enter a valid payment status.')
	 					newExpense = track.add(date, amount, category, payment, to, status, description)
	 					print('Expense added successfully:')
	 					print(newExpense)
	 					print(type(newExpense))
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

# 2. Users should be able to interact with the application through text-based commands and receive informative prompts and messages
