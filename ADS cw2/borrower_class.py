from book_class import Book

class Borrower:
    def __init__(self, first_name, last_name, account_number):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.username = None
        self.password = None
        self.rented_items = []
        self.fine_amount = 0.0

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def rent_item(self, item):
        if len(self.rented_items) < 8 and self.fine_amount == 0:
            self.rented_items.append(item)
            return True
        else:
            print("You have reached the maximum limit of rented items.")
            return False

    def return_item(self, item):
        if item in self.rented_items:
            self.rented_items.remove(item)
            return True
        else:
            print("Item not found in your rented items list.")
            return False

    def check_due_date(self):
        pass

    def pay_fine(self, amount):
        if amount >= self.fine_amount:
            self.fine_amount = 0
            print("Fine paid sucessfully.")
            return True
        else:
            self.fine_amount -= amount
            print(f"Fine partially paid. Remaining fine: {self.fine_amount}")
            return False

    def display_rented_items(self):
        print("Rented Items:")
        for item in self.rented_items:
            print(item.title)

