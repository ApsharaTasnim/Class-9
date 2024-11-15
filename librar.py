class Library:
    def __init__(self,list_of_books,name):
       self.booklist=list_of_books
       self.name=name
       self.lendDict={}
       
    def displayBooks(self):
        print(f"We have the following books in out library:{self.name}")
        for book in self.booksList:
            print(book)
            
    def lendBook(self,user,book):
        if book not in self.booksList:
            print("Sorry,we don't have that book.")
        elif book in self.lendDict:
            print("The book is already lent to someone.")
        else:
            self.lendDict[book]=user
            print(
                "Lender-Book database has been updated.You can take the book now."
            )
            
    
    def addBook(self,book):
        self.bookList.append(book)
        print(f"{book} ahs been added to the book list")
        
        
    def returnBook(self,book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("The book has been returned.")
        else:
            print("The was'nt not borrowed from us.")
            
            
if __name__ == '__main__':
    books =Library(['python','Harry Potter','It ends with us','It starts with us','Basics of C++'],"Let's Upskill")
    user_name=input("Welcome to our library!PLease enter your name:")
    
    
    while True:
        print(
            f"\nHello")