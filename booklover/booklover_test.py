import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`
        my_books = BookLover("Hannah", "hannah@virginia.edu", "romance") #initialize
        my_books.add_book("Pride and Prejudice", 4) #add a book
        book = "Pride and Prejudice"
        self.assertTrue(book in my_books.book_list)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        my_books = BookLover("Hannah", "hannah@virginia.edu", "romance") #initialize
        my_books.add_book("Pride and Prejudice", 4) #add a book
        self.assertRaises(ValueError, my_books.add_book("Pride and Prejudice", 4)) #see if adding same book twice throws error
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        my_books = BookLover("Hannah", "hannah@virginia.edu", "romance") #initialize
        my_books.add_book("Pride and Prejudice", 4) #add a book
        book = "Pride and Prejudice"
        self.assertTrue(my_books.has_read(book))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        my_books = BookLover("Hannah", "hannah@virginia.edu", "romance")
        my_books.add_book("Book Name", 2) #add a book
        book = "Pride and Prejudice"
        self.assertFalse(my_books.has_read(book))


    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        my_books = BookLover("Hannah", "hannah@virginia.edu", "romance")
        my_books.add_book("Book Name", 2)
        my_books.add_book("Pride and Prejudice", 4)
        expected = 2 
        actual = len(my_books.book_list)
        self.assertEqual(actual, expected) 
        

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        my_books = BookLover("Hannah", "hannah@virginia.edu", "romance")
        my_books.add_book("Book Name", 2)
        my_books.add_book("Pride and Prejudice", 4)
        my_books.add_book("Beloved", 5)
        x = my_books.fav_books()
        
        for val in x.values:
            if val[1] > 3: 
                self.assertTrue(True)
            else:
                self.assertTrue(False)

                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)


#run in the command line 
#1 set wd to where files exist
#2 python file_name.py in my case run "python3 booklover_test.py"


