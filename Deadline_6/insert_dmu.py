def dmu_seetry():
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


    # store all the data from the DMU table in a list
    mycursor.execute("SELECT * FROM DMU")
    dmu_list = mycursor.fetchall()
    #print(dmu_list)

    # Extracting the DMU ID of each element in dmu_list and storing it in a list
    dmu_id_list = [i[0] for i in dmu_list]
    #print(dmu_id_list)


    n = int(input("Enter number of DMUs to add (between 0 and 999): "))
    while(n > 999 or n < 0): # setting a limit of 999 rows to be inserted
        print("Invalid number of DMUs. Please enter a valid number of Dairy Farmers (between 0 and 999).")
        n = int(input("Enter number of DMUs to add: "))
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


        print("DMU", i+1, ":")
        dmu_id=""
        smf_id=""
        while(True):
            while(len(dmu_id)!=6):
                dmu_id = input("Enter DMU identification id (Enter 6 digit code): ")
            while(len(smf_id)!=3):
                smf_id = input("Enter SMF identification id (Enter 3 digit code): ")
            if(dmu_id[:3]==smf_id):
                break
            else:
                print("DMU id does not match with SMF id. Please enter a different DMU identification id.")
        while(dmu_id in dmu_id_list):
            print("DMU id already exists. Please enter a different DMU identification id.")
            while(True):
                while(len(dmu_id)!=6):
                    dmu_id = input("Enter DMU identification id (Enter 6 digit code): ")
                while(len(smf_id)!=3):
                    smf_id = input("Enter SMF identification id (Enter 3 digit code): ")
                if(dmu_id[:3]==smf_id):
                    break
                else:
                    print("DMU id does not match with SMF id. Please enter a different DMU identification id.")
        dmu_id_list.append(dmu_id) # to prevent inserting duplicate values by the user

        dmu_name = input("Enter DMU name: ")

        money = float(input("Enter money present: "))
        while(money > 999999999999.99 or money < 0):
            print("Invalid money value. Please enter a valid number (between 0 and 999999999999.99).")
            money = float(input("Enter money present: "))

        id_count = int(input("Enter batch id counter: "))
        while(id_count > 999999999999 or id_count < 0):
            print("Invalid batch id counter value. Please enter a valid number (between 0 and 999999999999).")
            id_count = int(input("Enter batch id counter: "))

        # append the values to the list
        values.append((dmu_id, dmu_name,money,id_count))
        print()



    # insert the data in values into the table
    sql = "INSERT INTO DMU VALUES (%s, %s, %s, %s, %s)"
    mycursor.executemany(sql, values)

    # commit the changes to the database
    mydb.commit()

    # print the number of rows affected
    print(mycursor.rowcount, "record(s) inserted.")
    print()



# close the connection
    mydb.close()
