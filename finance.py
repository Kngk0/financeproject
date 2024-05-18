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

		if choice == '1':
			#print('You selected Track expenses')
			track = expensetracking.expensetracker()
			# expensetracker.interface()
			# while expensetracker.interace is running, prompt user to add, remove, or update expense
				# if user enters add, they will be prompted to add expense information and the expense data will be updated and then displayed on the interface
				# if user enters remove, they will be prompted to remove expense information and the expense data will be updated and then displayed on the interface
				# if user enters update, they will be prompted to update expense and the expense data will be updated and then displayed on the interface
				# if user enters back, they will return to main menu
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
