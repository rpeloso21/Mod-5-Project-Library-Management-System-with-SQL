from connection_mysql import connect_database

conn = connect_database()
cursor = conn.cursor()

def return_username_for_library_id(id):
    query = "select * from users where library_id = %s"
    cursor.execute(query, (id,))
    for user in cursor.fetchall():
        return user[1]
    
# print(return_username_for_library_id("007"))

def return_author_name_for_author_id(id):
    query = "select * from authors where id = %s"
    cursor.execute(query, (id,))
    for author in cursor.fetchall():
        return author[1]
    
def return_author_id_for_name(author):
    query = "select * from authors where name = %s"
    cursor.execute(query, (author,))
    for author in cursor.fetchall():
        return author[0]
# print(return_author_id_for_name("Patrick rothfus"))
    
def return_genre_for_genre_id(id):
    query = "select * from genres where id = %s"
    cursor.execute(query, (id,))
    for genre in cursor.fetchall():
        return genre[1]

def return_genre_id_for_genre(genre):
    query = "select * from genres where name = %s"
    cursor.execute(query, (genre,))
    for author in cursor.fetchall():
        return author[0]


def return_bool_for_availability(x):
    if x == 1:
        return "True"
    else:
        return "False"

# print(return_genre_for_genre_id(1))
# print(return_author_name_for_author_id(1))

def return_book_id_for_title(title):
    query = "select * from books where title = %s"
    cursor.execute(query, (title,))
    for book in cursor.fetchall():
        return book[0]
    
def return_user_id_for_library_id(library_id):
    query = "select * from users where library_id = %s"
    cursor.execute(query, (library_id,))
    for user in cursor.fetchall():
        return user[0]
    
def return_borrow_id_for_title(title):
    id = return_book_id_for_title(title)
    query = "select * from borrowed_books where book_id = %s"
    cursor.execute(query, (id,))
    for item in cursor.fetchall():
        return(item[0])

# print(return_borrow_id_for_title("Theft of Swords"))

