# Inputting, categorizing, saving, and controlling expenses.

# 1. Users should be able to input their daily expenses, including the amount and category (e.g., groceries, utilities, entertainment).
class expensetracking: 
 	def __init__(self, user):
 		self.expense_item = []
 		self.user = user
 		self.tracking_info = 0.0

# 2. The application should allow users to add, remove, and update expenses.

# 3. Users should be able to view a summary of their expenses, categorized by expense type, and the total spending.