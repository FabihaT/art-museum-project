from DBTables import *

def guest_interface(cur):
    while True:  # Start of the main loop
        print("\nThis is a list of what you can browse.")
        print("1 - Art Pieces")
        print("2 - Artists")
        print("3 - Exhibitions")
        print("0 - Exit")
        selection = int(input("Select what you are looking for: "))

        if selection == 0:
            return

        if selection == 1:
            while True:
                subselection = input("Enter 1 for Sculptures, 2 for Paintings, and 3 for Other Pieces (0 to go back): ")
                if subselection == '1':
                    sculptures_info(cur)
                elif subselection == '2':
                    paintings_info(cur)
                elif subselection == '3':
                    other_info(cur)
                elif subselection == '0':
                    break  # Return to the main menu
                else:
                    print("Invalid selection. Please try again.")
        elif selection == 2:
            artist_info(cur)
        elif selection == 3:
            exhibition_info(cur)
        else:
            print("Invalid selection. Please try again.")
