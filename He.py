import tkinter as tk
from tkinter import messagebox
import csv

class PersonalFinanceTracker:
    """A simple personal finance tracker application."""

    def __init__(self, root):
        """Initialize the application."""
        self.root = root
        self.root.title("Personal Finance Tracker")

        # Variables
        self.records = []
        self.balance = 0.0

        # Frames
        self.frame_input = tk.Frame(root)
        self.frame_input.pack(pady=10)

        self.frame_summary = tk.Frame(root)
        self.frame_summary.pack(pady=10)

        # Input Widgets
        tk.Label(self.frame_input, text="Description:").grid(row=0, column=0, padx=5)
        self.entry_description = tk.Entry(self.frame_input, width=20)
        self.entry_description.grid(row=0, column=1, padx=5)

        tk.Label(self.frame_input, text="Amount:").grid(row=1, column=0, padx=5)
        self.entry_amount = tk.Entry(self.frame_input, width=20)
        self.entry_amount.grid(row=1, column=1, padx=5)

        self.type_var = tk.StringVar(value="Expense")
        tk.Radiobutton(self.frame_input, text="Income", variable=self.type_var, value="Income").grid(row=2, column=0)
        tk.Radiobutton(self.frame_input, text="Expense", variable=self.type_var, value="Expense").grid(row=2, column=1)

        self.button_add = tk.Button(self.frame_input, text="Add Record", command=self.add_record)
        self.button_add.grid(row=3, column=0, columnspan=2, pady=10)

        # Summary Widgets
        self.label_balance = tk.Label(self.frame_summary, text=f"Balance: ${self.balance:.2f}", font=("Arial", 14))
        self.label_balance.pack()

        self.button_view = tk.Button(self.frame_summary, text="View Records", command=self.view_records)
        self.button_view.pack(pady=5)

        self.button_save = tk.Button(self.frame_summary, text="Save Records", command=self.save_records)
        self.button_save.pack(pady=5)

        self.button_load = tk.Button(self.frame_summary, text="Load Records", command=self.load_records)
        self.button_load.pack(pady=5)

    def add_record(self):
        """Add a new record to the finance tracker."""
        try:
            description = self.entry_description.get()
            amount = float(self.entry_amount.get())
            record_type = self.type_var.get()

            if not description:
                raise ValueError("Description cannot be empty.")

            if record_type == "Expense":
                amount = -amount

            self.records.append({"Description": description, "Amount": amount})
            self.balance += amount
            self.update_balance()

            # Clear input fields
            self.entry_description.delete(0, tk.END)
            self.entry_amount.delete(0, tk.END)
            self.type_var.set("Expense")

            messagebox.showinfo("Success", "Record added successfully!")

        except ValueError as error:
            messagebox.showerror("Error", f"Invalid input: {error}")

    def update_balance(self):
        """Update the displayed balance."""
        self.label_balance.config(text=f"Balance: ${self.balance:.2f}")

    def view_records(self):
        """Display all records in a new window."""
        view_window = tk.Toplevel(self.root)
        view_window.title("Transaction Records")

        tk.Label(view_window, text="Description", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(view_window, text="Amount", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=10, pady=5)

        for i, record in enumerate(self.records, start=1):
            tk.Label(view_window, text=record["Description"]).grid(row=i, column=0, padx=10, pady=2)
            tk.Label(view_window, text=f"${record['Amount']:.2f}").grid(row=i, column=1, padx=10, pady=2)

    def save_records(self):
        """Save records to a CSV file."""
        try:
            with open("finance_records.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["Description", "Amount"])
                writer.writeheader()
                writer.writerows(self.records)
            messagebox.showinfo("Success", "Records saved to finance_records.csv")
        except Exception as error:
            messagebox.showerror("Error", f"Failed to save records: {error}")

    def load_records(self):
        """Load records from a CSV file."""
        try:
            with open("finance_records.csv", "r") as file:
                reader = csv.DictReader(file)
                self.records = []
                self.balance = 0.0

                for row in reader:
                    amount = float(row["Amount"])
                    self.records.append({"Description": row["Description"], "Amount": amount})
                    self.balance += amount

                self.update_balance()
            messagebox.showinfo("Success", "Records loaded successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No saved records found.")
        except Exception as error:
            messagebox.showerror("Error", f"Failed to load records: {error}")

# Create the application window
root = tk.Tk()
app = PersonalFinanceTracker(root)
root.mainloop()
