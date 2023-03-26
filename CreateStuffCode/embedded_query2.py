def seetry():
    import mysql.connector


    # connect to the database
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mysqlconnector10!!",
            database="All_Levels"
        )
    except:
        print("Connection failed.")
        print("Exiting...")
        exit()

    print("Connected to the database.")
    mycursor = mydb.cursor()


    # store all the data from the Dairy_Farmer table in a list
    mycursor.execute("SELECT * FROM Dairy_Farmer")
    dairy_farmer_list = mycursor.fetchall()
    #print(dairy_farmer_list)

    # Extracting the Dairy Farmer ID of each element in dairy_farmer_list and storing it in a list
    dairy_farmer_id_list = [i[0] for i in dairy_farmer_list]
    #print(dairy_farmer_id_list)


    n = int(input("Enter number of Dairy Farmers to add (between 0 and 999): "))
    while(n > 999 or n < 0): # setting a limit of 999 rows to be inserted
        print("Invalid number of Dairy Farmers. Please enter a valid number of Dairy Farmers (between 0 and 999).")
        n = int(input("Enter number of Dairy Farmers to add: "))
    print()

    # create a list of strings to store the values to be inserted into the table
    values = []


    if(n==0):
        print("No data to insert.")
        mydb.close()
        print("Exiting...")
        exit()

    # take input from the user
    for i in range(n):


        print("Farmer", i+1, ":")
        farmer_identification_id = input("Enter farmer identification id (Enter 3 digit number): ")
        farmer_identification_id = "FIC" + farmer_identification_id
        while(farmer_identification_id in dairy_farmer_id_list):
            print("Farmer identification id already exists. Please enter a different farmer identification id.")
            farmer_identification_id = input("Enter farmer identification id (Enter 3 digit number): ")
            farmer_identification_id = "FIC" + farmer_identification_id
        dairy_farmer_id_list.append(farmer_identification_id) # to prevent inserting duplicate values by the user

        milk_quantity = float(input("Enter milk quantity: "))
        while(milk_quantity > 999999999999.99 or milk_quantity < 0):
            print("Invalid milk quantity. Please enter a valid milk quantity (between 0 and 999999999999.99).")
            milk_quantity = float(input("Enter milk quantity: "))

        average_milk_quantity = float(input("Enter average milk quantity: "))
        while(average_milk_quantity > 999999999999.99 or average_milk_quantity < 0):
            print("Invalid average milk quantity. Please enter a valid average milk quantity (between 0 and 999999999999.99).")
            average_milk_quantity = float(input("Enter average milk quantity: "))

        cattlefeed = float(input("Enter cattle-feed (quantity):"))
        while(cattlefeed > 999999999999.99 or cattlefeed < 0):
            print("Invalid cattle-feed. Please enter a valid cattle-feed (between 0 and 999999999999.99).")
            cattlefeed = float(input("Enter cattle-feed (quantity):"))

        # append the values to the list
        values.append((farmer_identification_id, milk_quantity, average_milk_quantity, cattlefeed))
        print()



    # insert the data in values into the table
    sql = "INSERT INTO Dairy_Farmer (farmer_identification_id, milk_quantity, average_milk_quantity, cattlefeed) VALUES (%s, %s, %s, %s)"
    mycursor.executemany(sql, values)

    # commit the changes to the database
    mydb.commit()

    # print the number of rows affected
    print(mycursor.rowcount, "record(s) inserted.")
    print()



# close the connection
    mydb.close()








# mycursor.execute("SELECT * FROM Dairy_Farmer")
#
# for i in mycursor:
#     print(i)
#
# # insert ('FIC300', Decimal('50.00'), Decimal('30.00'), Decimal('0.00')) into the Dairy_Farmer table
# sql = """INSERT INTO Dairy_Farmer (farmer_identification_id, milk_quantity, average_milk_quantity, cattlefeed)
#         VALUES ("FIC300", 50.00, 30.00, 0.00)"""
#
# # write a parameterized query instead of hard-coded query
# sql = "INSERT INTO Dairy_Farmer (farmer_identification_id, milk_quantity, average_milk_quantity, cattlefeed) VALUES (%s, %s, %s, %s)"
# values = ("FIC301", 50.00, 30.00, 0.00)
#
# # execute the query
# mycursor.execute(sql, values)
#

