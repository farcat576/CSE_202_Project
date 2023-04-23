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
    vdcs_values = []
    vdcs_works_under_dmu_values = []

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

        vdcs_id_list.append(vdcs_id)  # to prevent inserting duplicate values by the user

        money = float(input("Enter money present: "))
        while (check_float_range(money) == False):
            print("Invalid money value.")
            money = float(input("Enter money present: "))

        cattle = float(input("Enter cattlefeed amount: "))
        while (check_float_range(cattle) == False):
            print("Invalid cattlefeed value.")
            cattle = int(input("Enter cattlefeed amount: "))

        milk_quantity = float(input("Enter milk quantity: "))
        while (check_float_range(milk_quantity) == False):
            print("Invalid milk quantity. Please enter a valid number (between 0 and 999999999999).")
            milk_quantity = int(input("Enter milk quantity: "))

        vdcs_name = input("Enter VDCS name: ")
        while (len(vdcs_name) > 20):
            print("Invalid VDCS name. Please enter a valid VDCS name.")
            vdcs_name = input("Enter VDCS name: ")


        # append the values to the list
        vdcs_values.append((vdcs_id, cattle, money, milk_quantity, vdcs_name))
        vdcs_works_under_dmu_values.append((vdcs_id, dmu_code))
        print()

    sql_insert_vdcs = "INSERT INTO VDCS VALUES (%s, %s, %s, %s, %s)"
    mycursor.executemany(sql_insert_vdcs, vdcs_values)


    print(mycursor.rowcount, "record(s) inserted in vdcs table.")
    print()

    sql_insert_vdcs_works_under_dmu = "INSERT INTO VDCS_Works_Under_DMU VALUES (%s, %s)"
    mycursor.executemany(sql_insert_vdcs_works_under_dmu, vdcs_works_under_dmu_values)

    print(mycursor.rowcount, "record(s) inserted in vdcs_works_under_dmu table.")
    print()

    mydb.commit()




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
    print("-------------------------------------------------------------------------------------")
    print("|VDCS Code|\t|Cattle Feed|\t|Money|\t|Milk Quantity|\t|Village Name|")
    print("-------------------------------------------------------------------------------------")
    print(vdcs_data[0][0], "\t\t", vdcs_data[0][1], "\t\t", vdcs_data[0][2], "\t\t", vdcs_data[0][3], "\t\t", vdcs_data[0][4], sep="")

    print()
    print()

def delete_VDCS(vdcs_code, cursor, mydb):
    mycursor = cursor
    get_df_code_sql = "SELECT farmer_identification_id FROM DF_Works_Under_VDCS WHERE vdcs_code = '{vdcs_coder}'".format(vdcs_coder=vdcs_code)
    mycursor.execute(get_df_code_sql)
    df_codes = mycursor.fetchall()
    print(df_codes)

    get_aadhar_sql = "SELECT aadhar_card_id FROM Dairy_Farmer_Possesses WHERE farmer_identification_id = '{df_coder}'"
    # print("Deleting Aadhar Cards")
    for df_code in df_codes:
        mycursor.execute(get_aadhar_sql.format(df_coder=df_code[0]))
        aadhar_card_id = mycursor.fetchall()[0][0]
        print(aadhar_card_id)
        delete_aa_sql = "DELETE FROM AADHAR_CARD WHERE aadhar_card_id = '{aadhar_number}'".format(aadhar_number=aadhar_card_id)
        mycursor.execute(delete_aa_sql)


    delete_df_sql = "DELETE FROM Dairy_Farmer WHERE farmer_identification_id = '{df_code}'"
    count = 0
    for df_code in df_codes:
        mycursor.execute(delete_df_sql.format(df_code=df_code[0]))
        count += mycursor.rowcount

    # print(count, "record(s) deleted from.")
    # print()


    sql = "DELETE FROM VDCS WHERE vdcs_code = '{vdcs_code}'".format(vdcs_code=vdcs_code)
    mycursor.execute(sql)

    print(mycursor.rowcount, "record(s) deleted.")
    print()

    mydb.commit()

def select_VDCS_In_DMU(dmu_chosen, cursor):
    mycursor = cursor
    query = """SELECT * FROM VDCS
                        NATURAL JOIN VDCS_Works_Under_DMU
                        WHERE VDCS_Works_Under_DMU.district_code = '{DMU}'""".format(DMU = dmu_chosen)


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
    vdcsin = int(input("Enter your choice: "))
    while (vdcsin > len(vdcs_data)+1 or vdcsin < 1):
        print("Invalid Dairy Farmer. Please enter a valid Dairy Farmer.")
        vdcsin = int(input("Enter your choice: "))
    if(vdcsin!=len(vdcs_data)+1):
        vdcs_chosen = vdcs_data[vdcsin - 1][0]
    else:
        vdcs_chosen=None

    return vdcs_chosen
