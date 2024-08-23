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

	# Function to set or update budget
	# FUNCTION setBudget(category STRING, budgetAmount FLOAT, description STRING)
		# DEFINE budget AS DICTIONARY OF CATEGORY, BUDGETAMOUNT, DESCRIPTION
		# FOR EACH budget IN self.budgetList
			# IF budget['category'] EQUALS category THEN
				# SET budget['budgetAmount'] TO budgetAmount
				# SET budget['remainingBudget'] TO budgetAmount
				# PRINT "Updated budget for " + category + ": " + budgetAmount
				# RETURN
			# END IF
		# END FOR

		# If category does not exist, add a new budget
		# CREATE newBudget AS BudgetCategory(category, monthlyBudget, description)
		# ADD newBudget to self.budgetList
		# PRINT 'Set new budget for ' + category + ": " + monthlyBudget
	# END FUNCTION