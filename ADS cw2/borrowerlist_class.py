class BorrowerListNode:
    def __init__(self, borrower):
        self.borrower = borrower
        self.prev = None
        self.next = None

class BorrowerList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_borrower(self, borrower):
        new_node = BorrowerListNode(borrower)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove_borrower(self, borrower):
        current = self.head
        while current:
            if current.borrower == borrower:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False

    def find_borrower_by_account_number(self, account_number):
        current = self.head
        while current:
            if current.borrower.account_number == account_number:
                return current.borrower
            current = current.next
        return None

    def display_all_borrowers(self):
        current = self.head
        while current:
            print("Borrower Account Number:", current.borrower.account_number)
            print("Name:", current.borrower.first_name, current.borrower.last_name)
            print("Username:", current.borrower.username)
            print("Password:", current.borrower.password)
            print("Rented Items:", [item.title for item in current.borrower.rented_items])
            print("---------------------------")
            current = current.next

