from DBTables import *

def guest_interface(cur):
    print("\nThis is a list of what you can browse.")
    print("1 - Art Pieces")
    print("2 - Artists")
    print("3 - Exhibitions")
    selection = int(input("Select what you are looking for (press 0 to exit): "))

    while(selection):
        if selection == 1:
            subselection = input("Enter 1 for Sculptures, 2 for Paintings, and 3 for Other Pieces: ")
            if subselection == '1':
                sculptures_info(cur)
            elif subselection == '2':
                paintings_info(cur)
            else:
                other_info(cur)
        elif selection == 2:
            artist_info(cur)
        elif selection == 3:
            exhibition_info(cur) 
        else:
            break  
        selection = int(input("\nEnter another selection to browse (press 0 to exit): "))

    if selection == 0:
        return