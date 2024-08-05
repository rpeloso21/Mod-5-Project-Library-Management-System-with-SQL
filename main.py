from connection_mysql import connect_database
from convert_input_functions import *
from validate_input_functions import *
from operations import *
import re

current_user = None
conn = connect_database()

def main():
    first_run = True
    while True:
        try:
            if first_run:
                print("\nWelcome to the library book management system!\n")
                user_id_input = input("Please enter your library ID (hint: '007'): ")
                if verify_user_id(user_id_input) == False:
                    print("That library ID was not found.  Please try again.")
                else:
                    current_user = user_id_input
                    print(f"\nWelcom {return_username_for_library_id(user_id_input)}")

            first_run = False
        except ValueError:
            print("Unexpected Value Error.  Please try again.")
            continue

        try:
            print("\nMain Menu: \n1. Book Operations \n2. User Operations \n3. Author Operations \n4. Genre Operations \n5. Change User \n6. Exit")
            operation_input = input("Please make a seletion: ")
            if operation_input == "1":
                book_operations(current_user)

            elif operation_input == "2":
                user_operations(current_user)

            elif operation_input == "3":
                author_operations()

            elif operation_input == "4":
                genre_operations()

            elif operation_input == "5":
                return_val = change_user(current_user)
                if return_val:
                    current_user = return_val
                    print(f"\nCurrent User updated to '{return_username_for_library_id(return_val)}'")

            elif operation_input == "6":
                break            

            else:
                print("That is not a valid selection.  Please try again.")
        
        except Exception as e:
            print(f"Unexpected Error: {e}")




if __name__ == "__main__":
    main()
                
