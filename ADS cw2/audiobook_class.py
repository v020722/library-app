from item_class import Item
from book_class import Book

class Audiobook(Book):
    def __init__(self, title, category, language, authors, year_published, narrator, duration):
        super().__init__(title, category, language, authors, year_published)
        self.narrator = narrator
        self.duration = duration

    def display_details(self):
        super().display_details()
        print(f"Narrator: {self.narrator}")
        print(f"Duration: {self.duration} minutes")

