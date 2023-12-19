import mysql.connector
from Guest import guest_interface
from Admin import admin_interface

def main():
    print("Welcome to the Art Database!")
    print("1 - DB Admin")
    print("2 - Browse as Guest")

    while True:
        selection = input("Please select your role from the above list: ")

        if selection == '1':
            username = input("Username: ")
            passcode = input("Password: ")
            break
        elif selection == '2':
            username = "guest"
            passcode = None 
            break
        else:
            print("Invalid Selection. Please try again.")

    cnx = mysql.connector.connect(
        host="localhost",
        port=3306,
        user=username,
        password=passcode,
        database="artdatabase"
    )

    try:
        cur = cnx.cursor(buffered=True)
        cur.execute("use artdatabase")

        if selection == '1':
            admin_interface(cur, cnx) 
        elif selection == '2':
            guest_interface(cur) 

    except mysql.connector.errors.DatabaseError as e:
        print(f"Database connection error: {e}")
    
    finally:
        cnx.close()
        print("\nThank you for using this application.")

if __name__ == "__main__":
    main()
