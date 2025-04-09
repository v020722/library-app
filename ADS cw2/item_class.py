class Item:
    def __init__(self, title, category, language, authors, year_published):
        self.title = title
        self.category = category
        self.language = language
        self.authors = authors
        self.year_published = year_published
    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Category: {self.category}")
        print(f"Language: {self.language}")
        print(f"Authors: {', '.join(self.authors)}")
        print(f"Year Published: {self.year_published}")