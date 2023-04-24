import mysql.connector

from check_float import *


def smf_seetry():



    # connect to the database
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mysqlconnector10!!",
            database="All_Levels"
        )
    except:
        print("Connection failedQ!@DASF.")
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


def display_SMF(smf_chosen, cursor):
    mycursor = cursor
    query = "SELECT * FROM SMF WHERE SMF_ID = '{smf_id}'".format(smf_id=smf_chosen)
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    print()
    print("SMF Chosen: ", smf_chosen, sep="")
    print("------------------------------------------------------------")
    print("State Code\t\tState Name\t\tSold\t\tCost")
    print("------------------------------------------------------------")
    print(myresult[0][0], "\t\t\t", myresult[0][1], "\t\t", myresult[0][2], "\t\t", myresult[0][3], sep="")

    print()
    print()

    return




def modify_SMF(smf_code, cursor, mydb):

    mycursor = cursor

    sold = float(input("Enter money gained by selling: "))
    while(check_float_range(sold) == False):
        print("Invalid sold value.")
        sold = float(input("Enter money gained by selling: "))

    cost = float(input("Enter money gained by producing: "))
    while(check_float_range(cost) == False):
        print("Invalid cost value.")
        cost = float(input("Enter money gained by producing: "))

    sql = "UPDATE SMF SET sold = %s, cost = %s WHERE state_code = %s"
    val = (sold, cost, smf_code)
    mycursor.execute(sql, val)

    print(mycursor.rowcount, "record(s) affected")
    print()

    mydb.commit()

    def run_transactions(data,mycursor,mydb):
    option = 0
    while (option != 5):
        print("1. Send 10000 in money to Surat DMU from Gujarat SMF")
        print("2. Delete all dairy farmers in Nani Naroli")
        print("3. Subtract 500 from all DMU transactions and add 500 to all SMF transactions")
        print("4. Set all Vets and Animal Husbandry Workers' salaries to a tenth of original amount from Anand DMU")
        print("5. Exit")
        print()
        option = int(input("Enter your choice: "))
        while (option > 15 or option < 1):
            print("Invalid option. Please enter a valid option.")
            option = int(input("Enter your choice: "))
        print()
        if (option == 1):
            try:
                mycursor.execute("""SET SQL_SAFE_UPDATES=0""")
                mycursor.execute("""UPDATE SMF set sold=sold-10000 WHERE state_code='GUJ'""")  
                print(mycursor.rowcount, "record(s) updated in SMF.") 
                mycursor.execute("""UPDATE DMU set money=money+10000 WHERE district_code='GUJSUR'""")
                print(mycursor.rowcount, "record(s) updated in DMU.") 
                mycursor.execute("""SET SQL_SAFE_UPDATES=1""")
                print("Updated !")  
                mydb.commit()
                print("Committed !") 
            except:  
                print("Can't update !")  
                mydb.commit() 
            print() 
        elif (option == 2):
            try:
                mycursor.execute("""SELECT COUNT(*) FROM Dairy_Farmer NATURAL JOIN DF_Works_Under_VDCS WHERE DF_Works_Under_VDCS.vdcs_code = 'SURNNN'""")
                print(mycursor.fetchall()[0][0], "record(s) present.")
                mycursor.execute("""DELETE from Dairy_Farmer where farmer_identification_id in (SELECT C.farmer_identification_id from (SELECT Dairy_Farmer.farmer_identification_id FROM Dairy_Farmer NATURAL JOIN DF_Works_Under_VDCS WHERE DF_Works_Under_VDCS.vdcs_code = 'SURNNN') as C)""")  
                print(mycursor.rowcount, "record(s) deleted.") 
                print("Deleted !")  
                mydb.rollback()
                print("Reverted !") 
                mycursor.execute("""SELECT COUNT(*) FROM Dairy_Farmer NATURAL JOIN DF_Works_Under_VDCS WHERE DF_Works_Under_VDCS.vdcs_code = 'SURNNN'""")
                print(mycursor.fetchall()[0][0], "record(s) present.") 
            except:  
                print("Can't delete !")  
                mydb.rollback() 
            print() 
        elif (option == 3):
            try:
                mycursor.execute("""SET SQL_SAFE_UPDATES=0""")
                mycursor.execute("""UPDATE DMU_Transaction set amount_sent=amount_sent-500""")  
                print(mycursor.rowcount, "record(s) updated in DMU_Transaction.") 
                mycursor.execute("""UPDATE SMF_Transaction set amount_sent=amount_sent+500""")
                print(mycursor.rowcount, "record(s) updated in SMF_Transaction.") 
                mycursor.execute("""SET SQL_SAFE_UPDATES=1""")
                print("Updated !")  
                mydb.commit()
                print("Committed !") 
            except:  
                print("Can't update !")  
                mydb.commit() 
            print()
        elif (option == 4):
            try:
                mycursor.execute("""SET SQL_SAFE_UPDATES=0""")
                mycursor.execute("""UPDATE VAHP SET salary=0.1*salary WHERE vah_id in (SELECT vahp_id from (SELECT vahp_id FROM VAHP NATURAL JOIN Works_Here WHERE Works_Here.vdcs_code in (Select vdcs_code from VDCS_Works_Under_DMU where district_code="GUJAND"))as C)""")  
                print(mycursor.rowcount, "record(s) updated.") 
                mycursor.execute("""SET SQL_SAFE_UPDATES=1""")
                print("Updated !")  
                mydb.rollback()
                print("Reverted !") 
            except:  
                print("Can't update !")  
                mydb.rollback() 
            print()
        else:
            break



















