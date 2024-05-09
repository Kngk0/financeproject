# user-friendly menu interface

# 1. The application should feature a command-line interface that is intuitive and easy to navigate.
def main_menu():
	while True:
		print('1. Track Expenses')
		print('2. Manage Budget')
		print('3. Calculator')
		print('4. Exit')

		choice = input('Enter your choice: ')

		if choice == '1':
			print('You selected Track expenses')
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
