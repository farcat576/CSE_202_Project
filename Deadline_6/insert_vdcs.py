import mysql.connector
from check_float import *


def insert_VDCS(dmu_code,cursor, mydb):


    mycursor = cursor

    # store all the data from the VDCS table in a list
    mycursor.execute("SELECT * FROM VDCS")
    vdcs_list = mycursor.fetchall()
    # print(vdcs_list)

    # Extracting the VDCS ID of each element in vdcs_list and storing it in a list
    vdcs_id_list = [i[0] for i in vdcs_list]
    # print(vdcs_id_list)

    n = int(input("Enter number of VDCSs to add (between 0 and 999): "))
    while (n > 999 or n < 0):  # setting a limit of 999 rows to be inserted
        print("Invalid number of VDCSs.")
        n = int(input("Enter number of VDCSs to add: "))
    print()

    # create a list of strings to store the values to be inserted into the table
    values = []

    if (n == 0):
        print("No data to insert.")
        print()
        return

    # take input from the user
    for i in range(n):

        print("VDCS", i + 1, ":")

        vdcs_id = input("Enter VDCS ID (3 letters): ")
        vdcs_id = dmu_code[3:] + vdcs_id.upper()
        while (len(vdcs_id) != 6 or vdcs_id in vdcs_id_list):
            print("Invalid VDCS ID. Please enter a valid VDCS ID.")
            vdcs_id = input("Enter VDCS ID (3 letters): ")
            vdcs_id = dmu_code[3:] + vdcs_id.upper()


        money = float(input("Enter money present: "))
        while (check_float_range(money) == False):
            print("Invalid money value.")
            money = float(input("Enter money present: "))

        cattle = int(input("Enter cattlefeed amount: "))
        while (check_float_range(cattle) == False):
            print("Invalid cattlefeed value.")
            cattle = int(input("Enter cattlefeed amount: "))

        milk_quantity = int(input("Enter milk quantity: "))
        while (check_float_range(milk_quantity) == False):
            print("Invalid milk quantity. Please enter a valid number (between 0 and 999999999999).")
            milk_quantity = int(input("Enter milk quantity: "))

        vdcs_name = input("Enter VDCS name: ")
        while (len(vdcs_name) > 20):
            print("Invalid VDCS name. Please enter a valid VDCS name.")
            vdcs_name = input("Enter VDCS name: ")


        # append the values to the list
        values.append((vdcs_id, cattle, money, milk_quantity, vdcs_name))
        print()

    sql = "INSERT INTO VDCS VALUES (%s, %s, %s, %s, %s)"
    mycursor.executemany(sql, values)

    mydb.commit()

    print(mycursor.rowcount, "record(s) inserted.")
    print()







def modify_VDCS(vdcs_code, cursor, mydb):

    mycursor = cursor


    cattlefeed = float(input("Enter cattle-feed (quantity):"))
    while(check_float_range(cattlefeed) == False):
        print("Invalid cattle-feed. Please enter a valid cattle-feed.")
        cattlefeed = float(input("Enter cattle-feed (quantity):"))

    money = float(input("Enter money: "))
    while(check_float_range(money) == False):
        print("Invalid money. Please enter a valid money.")
        money = float(input("Enter money: "))

    milk_quantity = float(input("Enter milk quantity: "))
    while(check_float_range(milk_quantity) == False):
        print("Invalid milk quantity. Please enter a valid milk quantity.")
        milk_quantity = float(input("Enter milk quantity: "))



    sql = "UPDATE VDCS SET Cattlefeed = %s, Money = %s, Milk_Quantity = %s WHERE VDCS_code = %s"
    val = (cattlefeed, money, milk_quantity, vdcs_code)
    mycursor.execute(sql, val)


    print(mycursor.rowcount, "record(s) modified.")
    print()

    mydb.commit()




def display_VDCS(vdcs_code, cursor):
    mycursor = cursor
    sql = "SELECT * FROM VDCS WHERE vdcs_code = '{vdcs_code}'".format(vdcs_code=vdcs_code)

    mycursor.execute(sql)
    vdcs_data = mycursor.fetchall()

    print()
    print("VDCS chosen: ", vdcs_code, sep="")
    print("------------------------------------------------------------")
    print("|VDCS Code|\t|Cattle Feed|\t|Money|\t|Milk Quantity|\t|Village Name|")
    print("------------------------------------------------------------")
    print(vdcs_data[0][0], "\t\t", vdcs_data[0][1], "\t\t", vdcs_data[0][2], "\t\t", vdcs_data[0][3], "\t\t", vdcs_data[0][4], sep="")

    print()
    print()



def select_VDCS_In_DMU(vdcs_chosen, cursor):
    mycursor = cursor
    query = """SELECT * FROM VDCS
                        NATURAL JOIN VDCS_Works_Under_DMU
                        WHERE VDCS_Works_Under_DMU.district_code = '{VDCS}'""".format(VDCS = vdcs_chosen)


    mycursor.execute(query)
    vdcs_data = mycursor.fetchall()


    print("VDCS available:")
    print("------------------------------------------------------------")
    print("|VDCS Code|")
    print("------------------------------------------------------------")
    count = 1
    for i in vdcs_data:
        print(count, ". ", i[0], sep="")
        count += 1
    print(count, ". ", "Back", sep="")
    dfin = int(input("Enter your choice: "))
    while (dfin > len(vdcs_data)+1 or dfin < 1):
        print("Invalid Dairy Farmer. Please enter a valid Dairy Farmer.")
        dfin = int(input("Enter your choice: "))
    if(dfin!=len(vdcs_data)+1):
        vdcs_chosen = vdcs_data[dfin - 1][0]
    else:
        vdcs_chosen=None

    return vdcs_chosen
