def exhibition_info(cur):
    instruction = 'select Start_date, End_date, Art_Desc, Cost, Status, Title from exhibitions join permanent_collection join artobj where exhibitions.ExID = permanent_collection.CollectID and exhibitions.ExID = artobj.ArtID'
    cur.execute(instruction)
    columns = cur.column_names
    search_result = cur.fetchall()
    print("\nSearch found ", len(search_result), " entries: \n")
    header_size = len(columns)
    for i in range(header_size):
        print("{:<20s}".format(columns[i]), end = '')
    print()
    print(25*header_size*'-')
    for row in search_result:
        for val in row:
            print("{:<20s}".format(str(val)), end = '')
        print()

def collections_info(cur):
    instruction = 'SELECT Name, CType, Description, Address, Phone, Contact_person FROM collections'
    cur.execute(instruction)
    columns = cur.column_names
    search_result = cur.fetchall()
    print("\nSearch found ", len(search_result), " entries: \n")
    for col in columns:
        print("{:<20s}".format(col), end='')
    print("\n" + '-' * 20 * len(columns))
    for row in search_result:
        for val in row:
            print("{:<20s}".format(str(val)), end='')
        print()

def permanent_collection_info(cur):
    instruction = 'SELECT CollectID, Date_acq, Status, Cost FROM permanent_collection'
    cur.execute(instruction)
    columns = cur.column_names
    search_result = cur.fetchall()
    print("\nSearch found ", len(search_result), " entries: \n")
    for col in columns:
        print("{:<30s}".format(col), end='')
    print("\n" + '-' * 30 * len(columns))
    for row in search_result:
        for val in row:
            print("{:<30s}".format(str(val)), end='')
        print()

def borrowed_info(cur):
    instruction = 'SELECT BorrowID, Collection, date_borrowed, date_return FROM borrowed'
    cur.execute(instruction)
    columns = cur.column_names
    search_result = cur.fetchall()
    print("\nSearch found ", len(search_result), " entries: \n")
    for col in columns:
        print("{:<30s}".format(col), end='')
    print("\n" + '-' * 30 * len(columns))
    for row in search_result:
        for val in row:
            print("{:<30s}".format(str(val)), end='')
        print()

def kept_in_info(cur):
    instruction = 'SELECT ArtID, Collect_name FROM kept_in'
    cur.execute(instruction)
    columns = cur.column_names
    search_result = cur.fetchall()
    print("\nSearch found ", len(search_result), " entries: \n")
    for col in columns:
        print("{:<30s}".format(col), end='')
    print("\n" + '-' * 30 * len(columns))
    for row in search_result:
        for val in row:
            print("{:<30s}".format(str(val)), end='')
        print()

def artist_info(cur):
    instruction = ''
    search = input("Enter the Artist name you are looking for (press ENTER to view all): ") or None
    if search == None:
        instruction = 'select Name, Birthdate, Date_died, Country_of_origin, Artist_Desc from artist'
        cur.execute(instruction)
    else:
        instruction = "select Name, Birthdate, Date_died, Country_of_origin, Artist_Desc from artist where Name = %(Name)s"
        cur.execute(instruction, {'Name':search})

    columns = cur.column_names
    search_result = cur.fetchall()
    print("\nSearch found ", len(search_result), " entries: \n")
    header_size = len(columns)
    for i in range(header_size):
        print("{:<30s}".format(columns[i]), end = '')
    print()
    print(30*header_size*'-')
    for row in search_result:
        for val in row:
            print("{:<30s}".format(str(val)), end = '')
        print()

def artobj_info(cur):
    instruction = ''
    search = input("Enter the ArtID you are looking for (press ENTER to view all): ") or None
    if search is None:
        instruction = 'SELECT ArtID, Art_Desc, Title, Artist, Art_yr, Origin, Epoch FROM artobj'
        cur.execute(instruction)
    else:
        instruction = "SELECT ArtID, Art_Desc, Title, Artist, Art_yr, Origin, Epoch FROM artobj WHERE ArtID = %(artid)s"
        cur.execute(instruction, {'artid': search})

    columns = cur.column_names
    search_result = cur.fetchall()
    print("\nSearch found ", len(search_result), " entries: \n")
    for col in columns:
        print("{:<20s}".format(col), end='')
    print("\n" + '-' * 20 * len(columns))
    for row in search_result:
        for val in row:
            print("{:<20s}".format(str(val)), end='')
        print()

def other_info(cur):
    instruction = ''
    search = input("Enter the ArtID you are looking for (press ENTER to view all): ") or None
    if search == None:
            instruction = 'select objType, Style, Art_yr, Artist, Title from artobj join other where artobj.ArtID = other.oID'
            cur.execute(instruction)
    else:
        instruction = "select objType, Style, Art_yr, Artist, Title from artobj join other where ArtID = %(artid)s and artobj.ArtID = other.oID"
        cur.execute(instruction, {'artid':search})

    columns = cur.column_names
    search_result = cur.fetchall()
    print("\nSearch found ", len(search_result), " entries: \n")
    header_size = len(columns)
    for i in range(header_size):
        print("{:<30s}".format(columns[i]), end = '')
    print()
    print(30*header_size*'-')
    for row in search_result:
        for val in row:
            print("{:<30s}".format(str(val)), end = '')
        print()

def paintings_info(cur):
    instruction = ''
    search = input("Enter the ArtID you are looking for (press ENTER to view all): ") or None

    if search == None:
        instruction = 'select Paint_type, Draw_on, Style, Artist, Title from artobj join painting where artobj.ArtID = painting.pID'
        cur.execute(instruction)
    else:
        instruction = "select Paint_type, Draw_on, Style, Artist, Title from artobj join painting where ArtID = %(artid)s and artobj.ArtID = painting.pID"
        cur.execute(instruction, {'artid':search})

    columns = cur.column_names
    search_result = cur.fetchall()
    print("\nSearch found ", len(search_result), " entries: \n")
    header_size = len(columns)
    for i in range(header_size):
        print("{:<25s}".format(columns[i]), end = '')
    print()
    print(30*header_size*'-')
    for row in search_result:
        for val in row:
            print("{:<25s}".format(str(val)), end = '')
        print()

def sculptures_info(cur):
    instruction = ''
    search = input("Enter the ArtID you are looking for (press ENTER to view all): ") or None
    if search == None:
        instruction = 'select Material, Height, Weight, Style, Artist, Title from artobj join sculpture where artobj.ArtID = sculpture.sID'
        cur.execute(instruction)
    else:
        instruction = "select Material, Height, Weight, Style, Artist, Title from artobj join sculpture where ArtID = %(artid)s and artobj.ArtID = sculpture.sID"
        cur.execute(instruction, {'artid':search})
    
    columns = cur.column_names
    search_result = cur.fetchall()
    print("\nSearch found ", len(search_result), " entries: \n")
    header_size = len(columns)
    for i in range(header_size):
        print("{:<25s}".format(columns[i]), end = '')
    print()
    print(30*header_size*'-')
    for row in search_result:
        for val in row:
            print("{:<25s}".format(str(val)), end = '')
        print()