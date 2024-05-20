# user-friendly menu interface
import expensetracking
# 1. The application should feature a command-line interface that is intuitive and easy to navigate.
def main_menu():
	while True:
		print('1. Track Expenses')
		print('2. Manage Budget')
		print('3. Calculator')
		print('4. Exit')

		choice = input('Enter your choice: ')
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
	 				print('7. Back')
	 				print('\n')
	 				choice = input('Enter your choice (1-7): ')

	 				if choice == '1':
	 					print('Please enter details of a new expense.')
	 					date = input('Enter the date of the expense (YYYY-MM-DD): ')
	 					amount = input('Enter the amount spent: ')
	 					category = input('Enter the category for this expense: ')
	 					description = input('Optionally, add a brief description for this expense:\n')
	 					payment = input('Specify the payment method: ')
	 					to = input('Enter the recipient: ')
	 					status = input('Paid or Pending: ')
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
