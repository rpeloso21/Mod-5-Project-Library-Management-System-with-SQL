from connection_mysql import connect_database
from convert_input_functions import *

conn = connect_database()

def fetch_user(name):
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "select * from users where name like %s"
            cursor.execute(query, (name,))
            for user in cursor.fetchall():
                print(f"\nName: {user[1]} \nID: {user[2]}")

        except Exception as e:
            print(f"Error: {e}")


def fetch_author(name):
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "select * from authors where name like %s"
            cursor.execute(query, (name,))
            for user in cursor.fetchall():
                print(f"\nName: {user[1]} \nBiography: {user[2]}")

        except Exception as e:
            print(f"Error: {e}")

def fetch_genre(name):
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "select * from genres where name like %s"
            cursor.execute(query, (name,))
            for user in cursor.fetchall():
                print(f"\nName: {user[1]} \nDescription: {user[2]} \nCategory: {user[3]}")

        except Exception as e:
            print(f"Error: {e}")


# Fetch Book Commands -------------------------------------------
def fetch_book(title):
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "select * from books where title like %s"
            cursor.execute(query, (title,))
            for book in cursor.fetchall():
                print(f"\nTitle: {book[1]} \nAuthor: {return_author_name_for_author_id(book[2])} \nGenre: {return_genre_for_genre_id(book[3])} \nISBN: {book[4]} \nPublication Date: {book[5]} \nIs Available: {return_bool_for_availability(book[6])} ")

        except Exception as e:
            print(f"Error: {e}")

def fetch_book_by_author(author):
    if conn is not None:
        try:
            author_id = return_author_id_for_name(author)
            cursor = conn.cursor()
            query = "select * from books where author_id like %s"
            cursor.execute(query, (author_id,))
            for book in cursor.fetchall():
                print(f"\nTitle: {book[1]} \nAuthor: {return_author_name_for_author_id(book[2])} \nGenre: {return_genre_for_genre_id(book[3])} \nISBN: {book[4]} \nPublication Date: {book[5]} \nIs Available: {return_bool_for_availability(book[6])} ")

        except Exception as e:
            print(f"Error: {e}")

def fetch_book_by_genre(genre):
    if conn is not None:
        try:
            genre_id = return_genre_id_for_genre(genre)
            cursor = conn.cursor()
            query = "select * from books where genre_id like %s"
            cursor.execute(query, (genre_id,))
            for book in cursor.fetchall():
                print(f"\nTitle: {book[1]} \nAuthor: {return_author_name_for_author_id(book[2])} \nGenre: {return_genre_for_genre_id(book[3])} \nISBN: {book[4]} \nPublication Date: {book[5]} \nIs Available: {return_bool_for_availability(book[6])} ")

        except Exception as e:
            print(f"Error: {e}")
# fetch_book_by_genre("high fantasy")

def fetch_book_by_ISBN(ISBN):
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "select * from books where ISBN like %s"
            cursor.execute(query, (ISBN,))
            for book in cursor.fetchall():
                print(f"\nTitle: {book[1]} \nAuthor: {return_author_name_for_author_id(book[2])} \nGenre: {return_genre_for_genre_id(book[3])} \nISBN: {book[4]} \nPublication Date: {book[5]} \nIs Available: {return_bool_for_availability(book[6])} ")

        except Exception as e:
            print(f"Error: {e}")

# fetch_book_by_genre("high fantasy")
            

def fetch_all_books():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = '''
            select b.title, a.name as Author, g.name as Genre, b.ISBN, b.publication_date, b.availability
            from books b, authors a, genres g
            where b.author_id = a.id and b.genre_id = g.id'''
            cursor.execute(query)
            print("List of Books: \n")
            for book in cursor.fetchall():
                print(book)

        except Exception as e:
            print(f"Error: {e}")

# fetch_all_books()

# fetch_book("the name of the wind")
