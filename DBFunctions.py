import mysql.connector

def get_table_name(table_selection):
    table_map = {
        '1': 'painting',
        '2': 'sculpture',
        '3': 'other',
        '4': 'artist',
        '5': 'exhibitions',
        '6': 'artobj',
        '7': 'collections',
        '8': 'permanent_collection',
        '9': 'borrowed',
        '10': 'kept_in'
    }
    return table_map.get(table_selection)

def insert(cur, cnx, table_selection):
    table_name = get_table_name(table_selection)
    if table_name:
        cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name='{table_name}'")
        columns = []
        input_val = []
        values = []
        for (column_name, data_type,) in cur:
            columns.append(column_name)
            input_val.append(data_type)

        for i in range(len(columns)):
            user_input = input(f"\nEnter a value for {columns[i]} (press ENTER if none): ")
            if user_input == '':
                values.append('NULL')
            elif input_val[i] == 'int':
                values.append(user_input)
            else:
                values.append(f"'{user_input}'")

        values_string = ', '.join(values)

        try:
            cur.execute(f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({values_string})")
            cnx.commit()  # Don't forget to commit your changes
            print("Insert operation was successful.")
        except mysql.connector.errors.IntegrityError as e:
            print(f"Insert unsuccessful due to foreign key constraint. Error: {e}")
        except mysql.connector.errors.ProgrammingError as e:
            print(f"Invalid syntax. Insert was unsuccessful. Error: {e}")
    else:
        print("Invalid table selection.")

def update(cur, cnx, table_selection):
    table_name = get_table_name(table_selection)
    if table_name:
        update_set = input("Enter the attributes and their values: ")
        update_where = input("Enter the tuples you would like to modify: ")
        try:
            cur.execute(f"UPDATE {table_name} SET {update_set} WHERE {update_where}")
            cnx.commit()
            print('Your table has been updated successfully.')
        except mysql.connector.errors.ProgrammingError:
            print("Invalid syntax. Update was unsuccessful.")
        except mysql.connector.errors.IntegrityError:
            print("Update unsuccessful due to foreign key constraint.")
    else:
        print("Invalid table selection.")

def delete(cur, cnx, table_selection):
    table_name = get_table_name(table_selection)
    if table_name:
        attribute = input("Enter the attribute to delete: ")
        value = input("Enter the value of your selected attribute to delete: ")
        try:
            cur.execute(f"DELETE FROM {table_name} WHERE {attribute}='{value}'")
            cnx.commit()
            print("Delete of tuple was successful.")
        except mysql.connector.errors.ProgrammingError:
            print("Invalid syntax. Delete was unsuccessful.")
        except mysql.connector.errors.IntegrityError:
            print("Delete unsuccessful due to foreign key constraint.")
    else:
        print("Invalid table selection.")