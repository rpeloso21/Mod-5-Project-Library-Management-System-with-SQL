from connection_mysql import connect_database


def add_author(name, biography):

    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "insert into authors (name, biography) values (%s, %s)"

            cursor.execute(query, (name, biography))
            conn.commit()
            print("New author added successfully.")

        except Exception as e:
            print(f"Error: {e}")


def add_book(title, author_id, genre_id, isbn, publication_date):

    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "insert into books (title, author_id, genre_id, isbn, publication_date) values (%s, %s, %s, %s, %s)"

            cursor.execute(query, (title, author_id, genre_id, isbn, publication_date))
            conn.commit()
            print("New book added successfully.")

        except Exception as e:
            print(f"Error: {e}")

# add_book("The Name of the Wind", 3, 1, "1111", "2003-05-11")


def add_genre(name, description, category):

    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "insert into genres (name, description, category) values (%s, %s, %s)"

            cursor.execute(query, (name, description, category))
            conn.commit()
            print("New genre added successfully.")

        except Exception as e:
            print(f"Error: {e}")


def add_user(name, library_id):

    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "insert into users (name, library_id) values (%s, %s)"

            cursor.execute(query, (name, library_id))
            conn.commit()
            print("New user added successfully.")

        except Exception as e:
            print(f"Error: {e}")

