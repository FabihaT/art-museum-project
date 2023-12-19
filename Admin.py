from DBTables import *
from DBFunctions import *

def admin_interface(cur, cnx):
    while True:
        print("\nCurrent Database tables:")
        print("1 - Paintings")
        print("2 - Sculptures")
        print("3 - Other Pieces")
        print("4 - Artists")
        print("5 - Exhibitions")
        print("6 - Art Objects")
        print("7 - Collections")
        print("8 - Permanent Collections")
        print("9 - Borrowed Items")
        print("10 - Kept In")
        table_selection = input("Select a table to modify (press 0 to exit): ")

        if table_selection == '0':
            return
        elif table_selection in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            display_table_data(cur, table_selection)
            modify_table_data(cur, cnx, table_selection)
        else:
            print("Invalid selection. Please try again.")

def display_table_data(cur, selection):
    if selection == '1':
        paintings_info(cur)
    elif selection == '2':
        sculptures_info(cur)
    elif selection == '3':
        other_info(cur)
    elif selection == '4':
        artist_info(cur)
    elif selection == '5':
        exhibition_info(cur)
    elif selection == '6':
        artobj_info(cur)
    elif selection == '7':
        collections_info(cur)
    elif selection == '8':
        permanent_collection_info(cur)
    elif selection == '9':
        borrowed_info(cur)
    elif selection == '10':
        kept_in_info(cur)

def modify_table_data(cur, cnx, table_selection):
    while True:
        print("\nChoose an operation for this table:")
        print("1 - Insert data")
        print("2 - Update data")
        print("3 - Delete data")
        print("0 - Go Back")
        operation = input("Select the operation: ")

        if operation == '1':
            insert(cur, cnx, table_selection)
        elif operation == '2':
            update(cur, cnx, table_selection)
        elif operation == '3':
            delete(cur, cnx, table_selection)
        elif operation == '0':
            return
        else:
            print("Invalid operation. Please try again.")