import mysql.connector
from check_float import *




def insert_DF(village_code,village_name,cursor,mydb):

    mycursor = cursor

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
    df_values = []
    df_works_under_VDCS_values = []
    df_possess_aadhar_values = []
    aadhar_values = []


    if(n==0):
        print("No data to insert.")
        print()
        return

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
        while(check_float_range(milk_quantity) == False):
            print("Invalid milk quantity. Please enter a valid milk quantity (between 0 and 999999999999.99).")
            milk_quantity = float(input("Enter milk quantity: "))

        average_milk_quantity = float(input("Enter average milk quantity: "))
        while(check_float_range(average_milk_quantity) == False):
            print("Invalid average milk quantity. Please enter a valid average milk quantity (between 0 and 999999999999.99).")
            average_milk_quantity = float(input("Enter average milk quantity: "))

        cattlefeed = float(input("Enter cattle-feed (quantity):"))
        while(check_float_range(cattlefeed) == False):
            print("Invalid cattle-feed. Please enter a valid cattle-feed (between 0 and 999999999999.99).")
            cattlefeed = float(input("Enter cattle-feed (quantity):"))

        # append the values to the list
        df_values.append((farmer_identification_id, milk_quantity, average_milk_quantity, cattlefeed))
        print()

        print("Enter Aadhar Details: ")
        aadhar_card_id = input("Enter Aadhar Card ID: ")
        while(len(aadhar_card_id) != 12):
            print("Invalid Aadhar Card ID. Please enter a valid Aadhar Card ID (12 digits).")
            aadhar_card_id = input("Enter Aadhar Card ID: ")

        person_name = input("Enter person name: ")
        while(len(person_name) > 50):
            print("Invalid person name. Please enter a valid person name (less than 50 characters).")
            person_name = input("Enter person name: ")

        age = int(input("Enter age: "))
        while(age > 110 or age < 0):
            print("Invalid age. Please enter a valid age (between 0 and 110).")
            age = int(input("Enter age: "))

        sex = input("Enter sex: ")
        while(sex.upper() not in ['M', 'F']):
            print("Invalid sex. Please enter a valid sex.")
            sex = input("Enter sex:")

        mobile_number = input("Enter mobile number: ")
        while(len(mobile_number) != 10):
            print("Invalid mobile number. Please enter a valid mobile number (10 digits).")
            mobile_number = input("Enter mobile number: ")

        address = input("Enter address: ")
        while(len(address) > 100):
            print("Invalid address. Please enter a valid address (less than 100 characters).")
            address = input("Enter address: ")

        bank_account_number = input("Enter bank account number: ")
        while(len(bank_account_number) != 16):
            print("Invalid bank account number. Please enter a valid bank account number (16 digits).")
            bank_account_number = input("Enter bank account number: ")

        place_of_birth = input("Enter place of birth: ")
        while(len(place_of_birth) > 50):
            print("Invalid place of birth. Please enter a valid place of birth (less than 50 characters).")
            place_of_birth = input("Enter place of birth: ")

        # append the values to the aadhar_values
        aadhar_values.append((aadhar_card_id,person_name,age,sex,mobile_number,address,bank_account_number,place_of_birth,village_name))

        # append the values to the df_works_under_VDCS_values
        df_works_under_VDCS_values.append((farmer_identification_id,village_code))

        # append the values to the df_possess_aadhar_values
        df_possess_aadhar_values.append((farmer_identification_id,aadhar_card_id))


    # insert the data in values into the dairy farmer table
    sql_insert_df = "INSERT INTO Dairy_Farmer VALUES (%s, %s, %s, %s)"
    sql_insert_aadhar = "INSERT INTO Aadhar_Card VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql_insert_df_works_under_VDCS = "INSERT INTO DF_Works_Under_VDCS VALUES (%s, %s)"
    sql_insert_df_possess_aadhar = "INSERT INTO Dairy_Farmer_Possesses VALUES (%s, %s)"

    mycursor.executemany(sql_insert_df, df_values)
    print(mycursor.rowcount, "record(s) inserted in dairy farmer table.")
    print()

    mycursor.executemany(sql_insert_aadhar, aadhar_values)
    print(mycursor.rowcount, "record(s) inserted in aadhar card table.")
    print()

    mycursor.executemany(sql_insert_df_works_under_VDCS, df_works_under_VDCS_values)
    print(mycursor.rowcount, "record(s) inserted in dairy farmer works under vdcs table.")
    print()

    mycursor.executemany(sql_insert_df_possess_aadhar, df_possess_aadhar_values)
    print(mycursor.rowcount, "record(s) inserted in dairy farmer possesses table.")
    print()

    mydb.commit()











def modify_DF(farmer_identification_id, cursor, mydb):

    mycursor = cursor


    # store all the data from the Dairy_Farmer table in a list
    mycursor.execute("SELECT * FROM Dairy_Farmer")
    dairy_farmer_list = mycursor.fetchall()
    #print(dairy_farmer_list)

    # Extracting the Dairy Farmer ID of each element in dairy_farmer_list and storing it in a list
    dairy_farmer_id_list = [i[0] for i in dairy_farmer_list]
    #print(dairy_farmer_id_list)

    milk_quantity = float(input("Enter milk quantity: "))
    while(check_float_range(milk_quantity) == False):
        print("Invalid milk quantity. Please enter a valid milk quantity.")
        milk_quantity = float(input("Enter milk quantity: "))

    average_milk_quantity = float(input("Enter average milk quantity: "))
    while(check_float_range(average_milk_quantity) == False):
        print("Invalid average milk quantity. Please enter a valid average milk quantity.")
        average_milk_quantity = float(input("Enter average milk quantity: "))

    cattlefeed = float(input("Enter cattle-feed (quantity):"))
    while(check_float_range(cattlefeed) == False):
        print("Invalid cattle-feed. Please enter a valid cattle-feed.")
        cattlefeed = float(input("Enter cattle-feed (quantity):"))

    sql = "UPDATE Dairy_Farmer SET Milk_Quantity = %s, Average_Milk_Quantity = %s, Cattlefeed = %s WHERE Farmer_Identification_Id = %s"
    val = (milk_quantity, average_milk_quantity, cattlefeed, farmer_identification_id)
    mycursor.execute(sql, val)


    print(mycursor.rowcount, "record(s) modified.")
    print()

    mydb.commit()



def display_DF(farmer_identification_id, cursor):
    mycursor = cursor
    sql = "SELECT * FROM Dairy_Farmer WHERE Farmer_Identification_Id = '{fid}'".format(fid=farmer_identification_id)

    mycursor.execute(sql)
    dairy_farmer_data = mycursor.fetchall()

    print()
    print("Dairy Farmer chosen: ", farmer_identification_id, sep="")
    print("------------------------------------------------------------")
    print("|DF Code|\t|Milk Quantity|\t|Avg Milk Qty|\t|Cattle Feed|")
    print("------------------------------------------------------------")
    #print(dairy_farmer_data)

    print(dairy_farmer_data[0][0], "\t\t", dairy_farmer_data[0][1], "\t\t\t",
          dairy_farmer_data[0][2], "\t\t\t", dairy_farmer_data[0][3])
    print()
    print()



def select_DF_In_VDCS(vdcs_chosen, cursor):
    mycursor = cursor
    query = """SELECT * FROM Dairy_Farmer
                        NATURAL JOIN DF_Works_Under_VDCS
                        WHERE DF_Works_Under_VDCS.vdcs_code = '{VDCS}'""".format(VDCS = vdcs_chosen)


    mycursor.execute(query)
    dairy_farmer_data = mycursor.fetchall()


    print("Dairy Farmers available:")
    print("------------------------------------------------------------")
    print("|DF Code|")
    print("------------------------------------------------------------")
    count = 1
    for i in dairy_farmer_data:
        print(count, ". ", i[0], sep="")
        count += 1
    print(count, ". ", "Back", sep="")
    dfin = int(input("Enter your choice: "))
    while (dfin > len(dairy_farmer_data)+1 or dfin < 1):
        print("Invalid Dairy Farmer. Please enter a valid Dairy Farmer.")
        dfin = int(input("Enter your choice: "))
    if(dfin!=len(dairy_farmer_data)+1):
        df_chosen = dairy_farmer_data[dfin - 1][0]
    else:
        df_chosen=None

    return df_chosen






def delete_DF(farmer_identification_id, cursor, mydb):
    mycursor = cursor
    sql = "DELETE FROM Dairy_Farmer WHERE Farmer_Identification_Id = '{fid}'".format(fid=farmer_identification_id)
    mycursor.execute(sql)
    print(mycursor.rowcount, "record(s) deleted.")

    mydb.commit()






def view_aadhar_details(df_chosen,cursor):
    mycursor = cursor
    query = """SELECT * FROM Aadhar_Card
                        NATURAL JOIN Dairy_Farmer_Possesses
                        WHERE Dairy_Farmer_Possesses.Farmer_Identification_Id = '{DF}'""".format(DF = df_chosen)

    mycursor.execute(query)
    aadhar_details = mycursor.fetchall()
    print()
    print("Aadhar Details:")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("|Aadhar Number|\t\t\t\t|Name|\t\t\t|Age|\t\t|Sex|\t\t|Mobile|\t\t|Address|\t|Bank No|\t\t|Place of Birth|\t|Village Name|")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(aadhar_details[0][0], "\t\t", aadhar_details[0][1], "\t\t", aadhar_details[0][2], "\t\t", aadhar_details[0][3], "\t\t",
            aadhar_details[0][4], "\t\t", aadhar_details[0][5], "\t\t", aadhar_details[0][6], "\t\t", aadhar_details[0][7], "\t\t",
            aadhar_details[0][8])
    print()
    print()

    return




















