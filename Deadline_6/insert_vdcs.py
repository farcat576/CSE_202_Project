def vdcs_seetry():
    import mysql.connector


    # connect to the database
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="farhan",
            database="All_Levels"
        )
    except:
        print("Connection failed.")
        print("Exiting...")
        exit()

    #print("Connected to the database.")
    mycursor = mydb.cursor()


    # store all the data from the VDCS table in a list
    mycursor.execute("SELECT * FROM VDCS")
    vdcs_list = mycursor.fetchall()
    #print(vdcs_list)

    # Extracting the VDCS ID of each element in vdcs_list and storing it in a list
    vdcs_id_list = [i[0] for i in vdcs_list]
    #print(vdcs_id_list)


    n = int(input("Enter number of VDCSs to add (between 0 and 999): "))
    while(n > 999 or n < 0): # setting a limit of 999 rows to be inserted
        print("Invalid number of VDCSs. Please enter a valid number of Dairy Farmers (between 0 and 999).")
        n = int(input("Enter number of VDCSs to add: "))
    print()

    # create a list of strings to store the values to be inserted into the table
    values = []


    if(n==0):
        print("No data to insert.")
        mydb.close()
        print("Exiting...")
        print()
        return

    # take input from the user
    for i in range(n):


        print("VDCS", i+1, ":")
        vdcs_id=""
        district_id=""
        while(true):
            while(len(vdcs_id)!=6):
                vdcs_id = input("Enter VDCS identification id (Enter 6 digit code): ")
            while(len(district_id)!=6):
                district_id = input("Enter DMU identification id (Enter 6 digit code): ")
            if(district_id[3:]==vdcs_id[:3]):
                break
            else:
                print("VDCS id does not match with DMU id. Please enter a different VDCS identification id.")
        while(vdcs_id in vdcs_id_list):
            print("VDCS id already exists. Please enter a different VDCS identification id.")
            while(true):
                while(len(vdcs_id)!=6):
                    vdcs_id = input("Enter VDCS identification id (Enter 6 digit code): ")
                while(len(district_id)!=6):
                    district_id = input("Enter DMU identification id (Enter 3 digit code): ")
                if(district_id[3:]==vdcs_id[:3]):
                    break
                else:
                    print("VDCS id does not match with DMU id. Please enter a different VDCS identification id.")
        vdcs_id_list.append(vdcs_id) # to prevent inserting duplicate values by the user

        vdcs_name = input("Enter VDCS name: ")

        money = float(input("Enter money present: "))
        while(money > 999999999999.99 or money < 0):
            print("Invalid money value. Please enter a valid number (between 0 and 999999999999.99).")
            money = float(input("Enter money present: "))

        cattle = int(input("Enter cattlefeed amount: "))
        while(cattle > 999999999999 or cattle < 0):
            print("Invalid cattlefeed value. Please enter a valid number (between 0 and 999999999999).")
            id_count = int(input("Enter cattlefeed amount: "))
        
        milk_quantity = int(input("Enter milk quantity: "))
        while(milk_quantity > 999999999999 or milk_quantity < 0):
            print("Invalid milk quantity. Please enter a valid number (between 0 and 999999999999).")
            milk_quantity = int(input("Enter milk quantity: "))

        # append the values to the list
        values.append((vdcs_id, district_id, cattle,money,milk_quantity, vdcs_name))
        print()



    # insert the data in values into the table
    sql = "INSERT INTO VDCS VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.executemany(sql, values)

    # commit the changes to the database
    mydb.commit()

    # print the number of rows affected
    print(mycursor.rowcount, "record(s) inserted.")
    print()



# close the connection
    mydb.close()
