class management:
	def __init__(self):
		# DEFINE budgetList AS LIST OF BUDGET_CATEGORY
		self.budgetList = []

	# Function to set budget
	def setBudget(self, category, budgetAmount, description = ' '):
		# DEFINE budget AS DICTIONARY OF CATEGORY, BUDGETAMOUNT, DESCRIPTION
		budget = {
			"Category": category,
			"Budget Amount": budgetAmount,
			"Description": description
		}

		categoryExist = False


		# FOR EACH budget IN self.budgetList
		for existingBudget in self.budgetList:
			# IF budget['category'] EQUALS category THEN
			if existingBudget['Category'] == category:
				# SET budget['budgetAmount'] TO budgetAmount
				existingBudget['Budget Amount'] = budgetAmount
				existingBudget['Description'] = description
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

		for key, value in budget.items():
			if key == "Budget Amount":
				print(f'{key}: ${value:,.2f}')
			else:
				print(f'{key}: {value}')

	# Mthod to view summary
	# FUNCTION viewSummary() RETURNS DICTIONARY
	def viewSummary(self, tracker):
		# DEFINE summary AS DICTIONARY WITH KEYS "Total Budgets", "Category Details"
		summary = {
			"Total Budget": 0,
			"Category Details": {}
		}

		# Initalize total budget to zero
		totalBudget = 0

		# Print budget entries and calculate total budget
		for budget in self.budgetList:
			# Initalize spent to zero
			spent = 0

			# Calculate remaining budget for each category
			for expense in tracker.expenses:
				if expense['Category'] == budget['Category']:
					spent += expense['Amount']

			remaining = budget['Budget Amount'] - spent

			summary["Category Details"][budget['Category']] = {
				"Budget": budget['Budget Amount'],
				"Spent": spent,
				"Remaining": remaining,
				"Description": budget["Description"]
			}
			totalBudget += budget["Budget Amount"]

		summary["Total Budget"] = f"${totalBudget:,.2f}"

		print("\nFinancial Summary:")
		print(f"Total Budget: {summary["Total Budget"]}")
		print(f"Category Details:")

		for category, details in summary["Category Details"].items():
			print(f"  Category: {category}")
			print(f"	Budget: ${details['Budget']:,.2f}")
			print(f"	Spent: ${details['Spent']:,.2f}")
			print(f"	Remaining: ${details['Remaining']:,.2f}")
			if details["Description"]:
				print(f"	Description: {details['Description']}")
			print()