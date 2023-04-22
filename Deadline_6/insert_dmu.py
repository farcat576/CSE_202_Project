import mysql.connector
from check_float import *


def insert_DMU():
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

def modify_DMU(dmu_code, cursor, mydb):

    mycursor = cursor


    money = float(input("Enter money present: "))
    while(money > 999999999999.99 or money < 0):
        print("Invalid money value. Please enter a valid number (between 0 and 999999999999.99).")
        money = float(input("Enter money present: "))

    id_count = int(input("Enter batch id counter: "))
    while(id_count > 999999999999 or id_count < 0):
        print("Invalid batch id counter value. Please enter a valid number (between 0 and 999999999999).")
        id_count = int(input("Enter batch id counter: "))



    sql = "UPDATE DMU SET money = %s, batch_id_counter = %s WHERE DMU_code = %s"
    val = (money, id_count, dmu_code)
    mycursor.execute(sql, val)


    print(mycursor.rowcount, "record(s) modified.")
    print()

    mydb.commit()




def display_DMU(district_code, cursor):
    mycursor = cursor
    sql = "SELECT * FROM DMU WHERE district_code = '{district_code}'".format(district_code=district_code)

    mycursor.execute(sql)
    dmu_data = mycursor.fetchall()

    print("DMU chosen: ", dmu_data[0][1], sep="")
    print("--------------------------------------------------------------")
    print("|Code|\t\t|Name|\t|Money|\t\t|Batch_Counter|\t|State Code|")
    print("--------------------------------------------------------------")
    print(dmu_data[0][0], "\t\t", dmu_data[0][1], "\t", dmu_data[0][2], "\t\t",
            dmu_data[0][3], "\t\t\t", dmu_data[0][0][:3])
    print()
    print()



def select_DMU_In_SMF(state_chosen, cursor):
    mycursor = cursor
    query = """SELECT * FROM DMU
                        NATURAL JOIN DMU_Works_Under_SMF
                        WHERE DMU_Works_Under_SMF.state_code = '{SMF}'""".format(SMF = state_chosen)


    mycursor.execute(query)
    dmu_data = mycursor.fetchall()


    print("DMUs available:")
    print("------------------------------------------------------------")
    print("|DMU Code|")
    print("------------------------------------------------------------")
    count = 1
    for i in dmu_data:
        print(count, ". ", i[0], sep="")
        count += 1
    print(count, ". ", "Back", sep="")
    dmuin = int(input("Enter your choice: "))
    while (dmuin > len(dmu_data)+1 or dmuin < 1):
        print("Invalid DMU. Please enter a valid Dairy Farmer.")
        dmuin = int(input("Enter your choice: "))
    if(dmuin!=len(dmu_data)+1):
        dmu_chosen = dmu_data[dmuin - 1][0]
    else:
        dmu_chosen=None

    return dmu_chosen

def delete_DMU(dmu_id, mycursor, mydb):
    sql = "DELETE FROM DMU WHERE district_code = '{fid}'".format(fid=dmu_id)
    mycursor.execute(sql)
    print(mycursor.rowcount, "record(s) deleted.")

    mydb.commit()
