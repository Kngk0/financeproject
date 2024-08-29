class management:
	def __init__(self):
		# Define data structures
		# DEFINE incomelist AS LIST OF INCOME
		self.incomeList = []
		# DEFINE budgetList AS LIST OF BUDGET_CATEGORY
		self.budgetList = []

	# Function to add income
	# FUNCTION add(date STRING, amount FLOAT, category STRING, incomeType STRING, source STRING, status STRING, description STRING)
	def add(self, date, amount, category, incomeType, source, status, description = ''):
		# DEFINE income AS DICTIONARY OF DATE, AMOUNT, CATEGORY, DESCRIPTION, INCOME TYPE, SOURCE, STATUS
		income = {
			"Date": date,
			"Amount": amount,
			"Category": category,
			"Description": description,
			"Income Type": incomeType,
			"Source": source,
			"Status": status
		}
		self.incomeList.append(income)
		for x, y in income.items():
			if x == "Amount":
				print(f'{x}: ${y:,.2f}')
			else:
				print(f'{x}: {y}')

	# Function to set budget
	# FUNCTION setBudget(category STRING, budgetAmount FLOAT, description STRING)
	def setBudget(self, category, budgetAmount, description = ' '):
		# DEFINE budget AS DICTIONARY OF CATEGORY, BUDGETAMOUNT, DESCRIPTION
		budget = {
			"Category": category,
			"Budget Amount": budgetAmount,
			"Remaining Budget": budgetAmount,
			"Description": description
		}

		categoryExist = False


		# FOR EACH budget IN self.budgetList
		for budget in self.budgetList:
			# IF budget['category'] EQUALS category THEN
			if budget['Category'] == category:
				# SET budget['budgetAmount'] TO budgetAmount
				budget['Budget Amount'] = budgetAmount
				# SET budget['remainingBudget'] TO budgetAmount
				budget['Remaining Budget'] = budgetAmount
				# PRINT "Updated budget for " + category + ": " + budgetAmount
				print(f"Updated budget for {category}: ${budgetAmount:,.2f}")
				categoryExist = True
				break
		# If category does not exist, add a new budget
		if not categoryExist:
			# ADD newBudget to self.budgetList
			self.budgetList.append(budget)
			# PRINT 'Set new budget for ' + category + ": " + monthlyBudget
			print(f"Set new budget for {category}: ${budgetAmount:,.2f}")

		for x, y in budget.items():
			if y == budgetAmount:
				print(f'{x}: ${y:,.2f}')
			else:
				print(f'{x}: {y}')

	# Function to view summary
	# FUNCTION viewSummary() RETURNS DICTIONARY
	def viewSummary(self):
		# DEFINE summary AS DICTIONARY WITH KEYS "Total Income", "Total Budgets", "Category Details"
		summary = {
			"Total Income": 0,
			"Total Budget": 0,
			"Category Details": {}
		}
		totalIncome = 0
		# Calculate total income
		# SET totalIncome TO SUM OF income.amount FOR EACH income IN self.incomeList
		for income in self.incomeList:
			print(f'Date: {income['Date']}')
 			print(f'Amount: {income['Amount']:,.2f}')
 			print(f'Category: {income['Category']}')
 			print(f'Description: {income['Description']}')
 			print(f'Income Type: {expense['Income Type']}')
 			print(f'Source: {expense['Source']}')
 			print(f'Status: {expense['Status']}')
 			print()
			totalIncome += income["Amount"]

		# SET summary["Total Income"] TO total_income
		summary['Total Income'] = f"${totalIncome:,.2f}"

		print(summary)