from item_class import Item

class Periodical(Item):
    def __init__(self, title, category, language, authors, year_published):
        super().__init__(title, category, language, authors, year_published)