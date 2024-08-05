    
from fetch_data_functions import *
from validate_input_functions import *
from add_data_functions import *
from convert_input_functions import *
from borrow_and_return_functions import *
from main  import *
import re
conn = connect_database()
cursor = conn.cursor()


def book_operations(current_user):

    book_operation_input = input("\nBook Operations \n1. Add a new book \n2. Borrow a book \n3. Return a book \n4. Search for a book \n5. Display all books \nPlease make a selection: ")
    
    if book_operation_input == "1":   #add book
        title = input("What is the title? ")
        while True:
            author_id = input("Please provide the author ID: ")
            if verify_author_id(author_id) == 1:
                break
            else:
                continue
        while True:
            genre_id = input("Please provide the genre ID: ")
            if verify_genre_id(genre_id) == 1:
                break
            else:
                continue
        while True:
            ISBN = input("Please provide the ISBN (4 digits): ")
            if len(ISBN) != 4:
                print("That is not a valid ISBN.")
                continue
            else:
                break
        while True:
            pub_date = input("Please provide the publication date (mm/dd/yyyy): ")
            if re.match("^(0[1-9]|1[0-2])/([0-2][0-9]|3[01])/\d{4}$", pub_date):
                break
            else:
                print("That is not a valid date format.  Please try again with (mm/dd/yyyy).")

        add_book(title, author_id, genre_id, ISBN, pub_date)
        print(f"\n'{title}' added successfully.")

    
    elif book_operation_input == "2":   #borrow book
        borrow_selection = input("What is the title of the book that you would like to borrow? ").lower()
        if verify_book_title(borrow_selection) == False:
            print("I'm sorry, that book is not in the library.")
        else:
            borrow_book(borrow_selection, current_user)


    elif book_operation_input == "3":   #return book
        return_selection = input("What is the name of the book that you would like to return? ").lower()
        if verify_book_title(return_selection) == False:
            print("I'm sorry, that book is not in the library.")
        else:
            return_book(return_selection)


    elif book_operation_input == "4":   #search for book
        method_of_search = input("How would you like to search our catalog? ('Title', 'Author', 'Genre', or 'ISBN'): ").lower()
        if method_of_search == "title":
            title = input("What is the title of the book that you would like to search for? ").lower()
            if verify_book_title(title) == False:
                print("I'm sorry, that book is not in the library.")
            else:
                fetch_book(title)  
        elif method_of_search == "author":
            authors = []
            author = input("What is the name of the author? ")
            query = "select * from authors"
            cursor.execute(query)
            for item in cursor.fetchall():
                authors.append(item[1].lower())
            if author.lower() not in authors:
                print("That authos is not in our library.")
            else:
                fetch_book_by_author(author)  
        elif method_of_search == "genre":
            genres = []
            genre = input("What is the name of the genre? ")
            query = "select * from genres"
            cursor.execute(query)
            for item in cursor.fetchall():
                genres.append(item[1].lower())
            if genre.lower() not in genres:
                print("That genre is not in our library.")
            else:
                fetch_book_by_genre(genre) 
        elif method_of_search == "isbn":
            ISBN = input("What is the ISBN? ")
            isbns = []
            query = "select * from books"
            cursor.execute(query)
            for item in cursor.fetchall():
                isbns.append(item[4])
            if ISBN not in isbns:
                print("That ISBN is not in our library.")
            else:
                fetch_book_by_ISBN(ISBN)

    elif book_operation_input == "5":   #view all books
        fetch_all_books()

    else:
        print("That is not a valid selection.  Please try again.")


def user_operations(current_user):

    user_operation_input = input("\nUser Operations \n1. Add a new user \n2. View user details \n3. Display all users \nPlease make a selection: ")

    if user_operation_input == "1":   #add a user
        user_name_input = input("What is your name? ")
        user_id_input = input("What is the user ID? ")
        add_user(user_name_input, user_id_input)
        print(f"\nUser '{user_name_input}' created successfully!")


    elif user_operation_input == "2":   #view user details
        view_user_input = input("Please enter the name of the user that you would like to view details on: ").lower()
        if verify_user_name(view_user_input) == False:
            print("That user is not in our system")
        else:
            fetch_user(view_user_input)
        
    elif user_operation_input == "3":   #view all users
        fetch_user("%")

    else:
        print("That is not a valid selection.  Please try again.")


def author_operations():

    author_operation_input = input("\nAuthor Operations \n1. Add a new author \n2. View author details \n3. Display all authors \nPlease make a selection: ")

    if author_operation_input == "1":   #add a author
        author_name_input = input("\nWhat is the autor's name? ")
        author_biography_input = input("Please provide the authors biography: ")
        add_author(author_name_input, author_biography_input)
        print(f"\nAuthor '{author_name_input}' created successfully!\n")


    elif author_operation_input == "2":   #view autor details
        view_author_input = input("Please enter the name of the author that you would like to view details on: ").lower()
        if verify_author_name(view_author_input) == False:
            print("That author is not in our system.")
        else:
            fetch_author(view_author_input)

    elif author_operation_input == "3":   #view all users
        fetch_author("%")

    else:
        print("That is not a valid selection.  Please try again.")



def genre_operations():

    genre_operation_input = input("\nGenre Operations \n1. Add a new genre \n2. View genre details \n3. Display all genres \nPlease make a selection: ")

    if genre_operation_input == "1":   #add a genre
        genre_name_input = input("\nWhat is the name of the genre? ")
        genre_description_input = input("Please provide a description of the genre: ")
        genre_category_input = input("What category is the genre in? ")
        
        add_genre(genre_name_input, genre_description_input, genre_category_input)
        print(f"\nGenre '{genre_name_input}' created successfully!")


    elif genre_operation_input == "2":   #view genre details
        view_genre_input = input("Please enter the name of the genre that you would like to view details on: ").lower()
        if verify_genre_name(view_genre_input) == False:
            print("That genre is not in our library.")
        else:
            fetch_genre(view_genre_input)

    elif genre_operation_input == "3":   #view all genres
        fetch_genre("%")

    else:
        print("That is not a valid selection.  Please try again.")

    
def change_user(current_user):
    change_user_input = input("What is the library ID of the user that you would like to change to? ")

    if verify_user_id(change_user_input) == False:
        print("That is not a valid library ID.")
        return None
    else:
        return change_user_input

    
