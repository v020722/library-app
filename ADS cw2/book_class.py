from item_class import Item

class Book(Item):
    def __init__(self, title, category, language, authors, year_published, isbn=None):
        super().__init__(title, category, language, authors, year_published)
        self.isbn = isbn

    def display_details(self):
        super().display_details()
        if self.isbn:
            print(f"ISBN: {self.isbn}")