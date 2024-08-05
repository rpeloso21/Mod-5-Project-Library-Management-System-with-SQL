from connection_mysql import connect_database

conn = connect_database()
cursor = conn.cursor()

def verify_book_title(title):
    all_titles = []

    query = "select * from books"
    cursor.execute(query)
    for book in cursor.fetchall():
        all_titles.append(book[1].lower())

    if title.lower() in all_titles:
        return True
    else:
        return False
# print(verify_book_title("The Name of the Wind"))

def verify_author_id(author_id):
    all_ids = []

    query = "select * from authors"
    cursor.execute(query)
    for author in cursor.fetchall():
        all_ids.append(author[0])

    if int(author_id) in all_ids:
        return True
    else:
        return False
    
def verify_genre_id(genre_id):
    all_ids = []

    query = "select * from genres"
    cursor.execute(query)
    for genre in cursor.fetchall():
        all_ids.append(genre[0])

    if int(genre_id) in all_ids:
        return True
    else:
        return False
    
def verify_user_id(user_id):
    all_ids = []

    query = "select * from users"
    cursor.execute(query)
    for user in cursor.fetchall():
        all_ids.append(user[2])

    if (user_id) in all_ids:
        return True
    else:
        return False
    
def verify_user_name(username):
    all_user_names = []

    query = "select * from users"
    cursor.execute(query)
    for user in cursor.fetchall():
        all_user_names.append(user[1].lower())

    if username.lower() in all_user_names:
        return True
    else:
        return False
    
def verify_author_name(author_name):
    all_author_names = []

    query = "select * from authors"
    cursor.execute(query)
    for author in cursor.fetchall():
        all_author_names.append(author[1].lower())

    if author_name.lower() in all_author_names:
        return True
    else:
        return False

def verify_genre_name(genre_name):
    all_genre_names = []

    query = "select * from genres"
    cursor.execute(query)
    for genre in cursor.fetchall():
        all_genre_names.append(genre[1].lower())

    if genre_name.lower() in all_genre_names:
        return True
    else:
        return False