class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        print("Title:", self.title)

    def get_author(self):
        print("Author:", self.author)

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author
        
    def display_info(self):
        self.get_title()
        self.get_author()

class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.number_pages = number_pages

    def get_number_of_pages(self):
        print("Number of pages:", self.number_pages)

    def set_number_of_pages(self, number_pages):
        self.number_pages = number_pages

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        self.issue_number = issue_number
        super().__init__(title, author)

    def get_issue_number(self):
        print("Issue number:", self.issue_number)

    def set_issue_number(self, issue_number):
        self.issue_number = issue_number

pub1 = Publication("Story","Me")
book1 = Book("Story2","You","123")


#magazine goes here

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.display_info()
book1.get_number_of_pages()
