def smf_seetry():
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


    # store all the data from the SMF table in a list
    mycursor.execute("SELECT * FROM SMF")
    smf_list = mycursor.fetchall()
    #print(smf_list)

    # Extracting the SMF ID of each element in smf_list and storing it in a list
    smf_id_list = [i[0] for i in smf_list]
    #print(smf_id_list)


    n = int(input("Enter number of SMFs to add (between 0 and 999): "))
    while(n > 999 or n < 0): # setting a limit of 999 rows to be inserted
        print("Invalid number of SMFs. Please enter a valid number of Dairy Farmers (between 0 and 999).")
        n = int(input("Enter number of SMFs to add: "))
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


        print("SMF", i+1, ":")
        smf_id=""
        while(len(smf_id)!=3):
            smf_id = input("Enter SMF identification id (Enter 3 digit code): ")
        while(smf_id in smf_id_list):
            print("SMF id already exists. Please enter a different SMF identification id.")
            while(len(smf_id)!=3):
                smf_id = input("Enter SMF id (Enter 3 digit code): ")
        smf_id_list.append(smf_id) # to prevent inserting duplicate values by the user

        smf_name = input("Enter SMF name: ")

        sold = float(input("Enter money gained by selling: "))
        while(sold > 999999999999.99 or sold < 0):
            print("Invalid sold value. Please enter a valid number (between 0 and 999999999999.99).")
            sold = float(input("Enter money gained by selling: "))

        cost = float(input("Enter money gained by producing: "))
        while(cost > 999999999999.99 or cost< 0):
            print("Invalid cost value. Please enter a valid number (between 0 and 999999999999.99).")
            cost = float(input("Enter money gained by producing: "))

        # append the values to the list
        values.append((smf_id, smf_name,sold,cost))
        print()



    # insert the data in values into the table
    sql = "INSERT INTO SMF VALUES (%s, %s, %s, %s)"
    mycursor.executemany(sql, values)

    # commit the changes to the database
    mydb.commit()

    # print the number of rows affected
    print(mycursor.rowcount, "record(s) inserted.")
    print()



# close the connection
    mydb.close()