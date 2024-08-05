from connection_mysql import connect_database
from convert_input_functions import *
conn = connect_database()
cursor = conn.cursor()




def borrow_book(book_title, current_user):
    query1 = "select * from books where title = %s"
    cursor.execute(query1, (book_title,))
    if cursor.fetchone()[6] == 0:
        print("That books is not available")
    
    else:
        #update book table
        query2 = "update books set availability = False where title like %s"
        cursor.execute(query2, (book_title,))
        conn.commit()
        print(f"'{book_title}' checked out successfully.")

        #update borrowed_books table
        user_id = return_user_id_for_library_id(current_user)
        book_id = return_book_id_for_title(book_title)
        borrow_date = "2024-08-04"
        return_date = "2024-08-14"

        query3 = "insert into borrowed_books (user_id, book_id, borrow_date, return_date) values (%s, %s, %s, %s)"
        cursor.execute(query3, (user_id, book_id, borrow_date, return_date))
        conn.commit()

def return_book(book_title):
    #update book table
    query = " update books set availability = True where title like %s"
    cursor.execute(query, (book_title,))
    conn.commit()
    print(f"'{book_title}' returned successfully.")

    #update borrowed_books table
    id = return_borrow_id_for_title(book_title)
    query2 = "delete from borrowed_books where id = %s"
    cursor.execute(query2, (id,))
    conn.commit()


        


# borrow_book("Theft of Swords", current_user)
# return_book("Theft of Swords")