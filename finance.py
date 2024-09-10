# user-friendly menu interface
import transactionTracking
import budgetmanagement
import datetime
# 1. The application should feature a command-line interface that is intuitive and easy to navigate.
# 2. Users should be able to interact with the application through text-based commands and receive informative prompts and messages
def mainMenu():
	track = transactionTracking.transactionTracker()
	manage = budgetmanagement.management()
	while True:
		print('==============================')
		print('Main Menu')
		print('==============================')
		print('1. Track Transactions')
		print('2. Manage Budget')
		print('3. Calculator')
		print('4. Exit\n')
		choice = input('Enter your choice (1-4): ')
		print()
		if choice.strip():
			if choice == '1':
				while True:
	 				print('==============================')
	 				print('Transaction Tracker Menu')
	 				print('==============================')
	 				print('1. Add Expense')
	 				print('2. Add Income')
	 				print('3. View Transactions')
	 				print('4. Search Transactions')
	 				print('5. Back\n')
	 				choice = input('Enter your choice (1-5): ')
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
	 					if date > datetime.datetime.today().date():
	 						payment_status = 'pending'
	 					else:
	 						payment_status = 'paid'
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
	 					print('\nExpense added successfully:')
	 					track.addExpense(date, amount, category, payment, to, payment_status, description)
	 					print()
	 				elif choice == '2':
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
	 					track.addIncome(date, amount, category, type, source, status, description)
	 					print()
	 				elif choice == '3':
	 					track.view()
	 					# Check if both expenses and incomes are empty
	 					if not track.expenses and not track.incomes:
	 						print('No transactions to show.\n')
	 				elif choice == '4':
	 					while True:
	 						search = input('Search (or type "exit" to quit): ')
	 						if search.lower() == 'exit':
	 							break
	 						track.search(search)
	 						print()
	 				elif choice == '5':
	 					break
	 				else:
	 					print('Please enter a valid choice (1-4)\n')
			elif choice == '2':
				print('You selected Manage Budget')
				while True:
					print('==============================')
					print('Budget Management Menu')
					print('==============================')
					print('1. Set or Update Budget')
					print('2. View Budget')
					print('3. Back\n')
					choice = input('Enter your choice (1-3): ')
					print()
					if choice == '1':
						print('Please enter details for Budget')
						while True:
							category = input('Enter the Budget category: ').strip()
							if not category:
								print('Please enter the category for this Budget.')
							else:
								break
						while True:
							budgetAmount = input("Enter the Budget amount: $")
							if not budgetAmount:
								print('Please enter the amount for this Budget')
								continue
							try:
								budgetAmount = float(budgetAmount.replace(',',''))
								if budgetAmount <= 0:
									print('Amount must be a positive number.')
								else:
									break
							except ValueError:
								print('Invalid amount. Please enter a valid number.')
						description = input("Enter a description for the Budget (optional): ")
						if not description:
							print('No description provided for this Budget.')
						print('\nBudget set successfully:')
						manage.setBudget(category, budgetAmount, description)
						print()
					elif choice == '2':
						manage.viewSummary(track)
						print()
					elif choice == '3':
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


mainMenu()