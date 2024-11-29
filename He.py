class ExpenseTracker:
    """Class for tracking expenses."""
 
    def __init__(self):
        """Initialize an empty expense list."""
        self.expenses = []  # List to store expenses as tuples (name, amount)
 
    def add_expense(self, name, amount):
        """Add a new expense.
 
        Args:
            name (str): Name of the expense.
            amount (str): Amount of the expense, should be convertible to float.
 
        Raises:
            ValueError: If the name is empty or the amount is invalid.
        """
        try:
            amount = float(amount)
            if not name or amount <= 0:
                raise ValueError(
                    "Expense name must not be empty, and amount must be positive."
                )
            self.expenses.append((name, amount))
        except ValueError as e:
            raise ValueError("Invalid expense name or amount.") from e
 
    def get_expenses(self):
        """Retrieve the list of expenses.
 
        Returns:
            list: A list of tuples containing expense name and amount.
        """
        return self.expenses
 
    def delete_expense(self, index):
        """Delete an expense by its index.
 
        Args:
            index (int): Index of the expense to delete.
 
        Raises:
            IndexError: If the index is invalid.
        """
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
        else:
            raise IndexError("Invalid expense index.")
 
 
def main():
    """Main function to run the Expense Tracker."""
    tracker = ExpenseTracker()
 
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
 
        if choice == "1":
            # Add Expense
            name = input("Enter expense name: ").strip()
            amount = input("Enter expense amount: ").strip()
            try:
                tracker.add_expense(name, amount)
                print("Expense added successfully!")
            except ValueError as e:
                print(f"Error: {e}")
 
        elif choice == "2":
            # View Expenses
            expenses = tracker.get_expenses()
            if expenses:
                print("\nExpenses:")
                for idx, (name, amount) in enumerate(expenses, start=1):
                    print(f"{idx}. {name}: ${amount:.2f}")
            else:
                print("No expenses found.")
 
        elif choice == "3":
            # Delete Expense
            expenses = tracker.get_expenses()
            if not expenses:
                print("No expenses to delete.")
                continue
 
            print("\nExpenses:")
            for idx, (name, amount) in enumerate(expenses, start=1):
                print(f"{idx}. {name}: ${amount:.2f}")
 
            try:
                index = int(input("Enter the expense number to delete: ")) - 1
                tracker.delete_expense(index)
                print("Expense deleted successfully!")
            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")
 
        elif choice == "4":
            # Exit Program
            print("Exiting Expense Tracker. Goodbye!")
            break
 
        else:
            print("Invalid choice. Please try again.")
 
 
if __name__ == "__main__":
    main()
