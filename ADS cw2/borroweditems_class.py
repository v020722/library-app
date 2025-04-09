class BorrowedItems:
    def __init__(self, borrower_account_num, item_borrowed, date_borrowed):
        self.borrower_account_num = borrower_account_num
        self.item_borrowed = item_borrowed
        self.date_borrowed = date_borrowed
        self.next = None
        self.prev = None

    def __str__(self):
        return f"Borrower Account Number: {self.borrower_account_num}, Item Borrowed: {self.item_borrowed}, Date Borrowed: {self.date_borrowed}"

class BorrowedItemsLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_borrowed_item(self, borrower_account_num, item_borrowed, date_borrowed):
        new_item = BorrowedItems(borrower_account_num, item_borrowed, date_borrowed)
        if not self.head:
            self.head = new_item
            self.tail = new_item
        else:
            self.tail.next = new_item
            new_item.prev = self.tail
            self.tail = new_item

    def display_borrowed_items(self):
        current = self.head
        while current:
            print(current)
            current = current.next