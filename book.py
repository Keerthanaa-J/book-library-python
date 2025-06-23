class Book:
    def __init__(self,title,author,year_published,checked_out):
        self.title=title
        self.author=author
        self.year_published=year_published
        self.checked_out=checked_out
        
    def display(self):
        print("Title of the book is:",self.title)
        print("Author of the book is:",self.author)
        print("Year of publication is:",self.year_published)
        print("checkout of book(true or false): ",self.checked_out)
        print("_____________________________________________________________")

    def checkout(self):
        self.checked_out=True
        print("book is taken from library",self.checked_out)
        print("______________________________________________________________")

    def return_book(self):
        self.checked_out=False
        print("book is back in library",self.checked_out)
        print("______________________________________________________________")

book1=Book("Aram","Jeyamohan",2001,True)
book2=Book("One Indian Girl","Chethan Bhagat",2016,False)

print("Initial info")
book1.display()
book2.display()

print("Before checking the book")
book1.checkout()
book1.display()
book2.checkout()
book2.display()

print("After returning the book")
book1.return_book()
book1.display()
book2.return_book()
book2.display()
        
        
        
        