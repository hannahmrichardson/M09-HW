import pandas as pd
class BookLover: 
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})): 
        self.name = name 
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        
    def add_book(self, book_name, rating):
        rating_values = [0,1,2,3,4,5]
        
        if (book_name not in self.book_list['book_name'].values):
            if rating in rating_values:
                new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
                })
        
                self.book_list = pd.concat([self.book_list,new_book], ignore_index=True)
                self.num_books += 1
            else: 
                raise ValueError("Rating must be between 0 and 5")
        else: 
            raise ValueError("The book provided is already in your list")

    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            return True 
        else:
            return False
        
    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        fav_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        for book in self.book_list.values:
            if book[1]  > 3:
                fav_book = pd.DataFrame({
                'book_name': [book[0]], 
                'book_rating': [book[1]]
                })
                fav_list = pd.concat([fav_list,fav_book], ignore_index=True)

        return fav_list

        
        