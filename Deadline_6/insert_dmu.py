import mysql.connector
from check_float import *


def check_float_range(num):
    if(num > 999999999999.99 or num < 0):
        return False
    return True


def insert_DMU(smf_code, cursor, mydb):


    mycursor = cursor


    # store all the data from the DMU table in a list
    mycursor.execute("SELECT * FROM DMU")
    dmu_list = mycursor.fetchall()
    #print(dmu_list)

    # Extracting the DMU ID of each element in dmu_list and storing it in a list
    dmu_id_list = [i[0] for i in dmu_list]
    #print(dmu_id_list)


    n = int(input("Enter number of DMUs to add (between 0 and 999): "))
    while(n > 999 or n < 0): # setting a limit of 999 rows to be inserted
        print("Invalid number of DMUs.")
        n = int(input("Enter number of DMUs to add: "))
    print()

    # create a list of strings to store the values to be inserted into the table
    dmu_values = []
    dmu_works_under_smf_values = []


    if(n==0):
        print("No data to insert.")
        print()
        return

    # take input from the user
    for i in range(n):


        print("DMU", i+1, ":")

        dmu_id = input("Enter DMU ID (3 letters): ")
        dmu_id = smf_code + dmu_id.upper()
        while(len(dmu_id) != 6 or dmu_id in dmu_id_list):
            print("Invalid DMU ID. Please enter a valid DMU ID.")
            dmu_id = input("Enter DMU ID (3 letters): ")
            dmu_id = smf_code + dmu_id.upper()

        dmu_id_list.append(dmu_id) # to prevent inserting duplicate values by the user

        dmu_name = input("Enter DMU name: ")
        while(len(dmu_name) > 30):
            print("Invalid DMU name. Please enter a valid name (less than 30 characters).")
            dmu_name = input("Enter DMU name: ")


        money = float(input("Enter money present: "))
        while(check_float_range(money) == False):
            print("Invalid money value. Please enter a valid number (between 0 and 999999999999.99).")
            money = float(input("Enter money present: "))

        id_count = int(input("Enter batch id counter: "))
        while(check_float_range(id_count) == False):
            print("Invalid batch id counter value. Please enter a valid number (between 0 and 999999999999).")
            id_count = int(input("Enter batch id counter: "))

        # append the values to the list
        dmu_values.append((dmu_id, dmu_name,money,id_count))
        dmu_works_under_smf_values.append((dmu_id, smf_code))
        print()



    # insert the data in values into the table
    sql = "INSERT INTO DMU VALUES (%s, %s, %s, %s)"
    mycursor.executemany(sql, dmu_values)

    print(mycursor.rowcount, "record(s) inserted in dmu table.")
    print()

    sql = "INSERT INTO DMU_Works_Under_SMF VALUES (%s, %s)"
    mycursor.executemany(sql, dmu_works_under_smf_values)

    print(mycursor.rowcount, "record(s) inserted in dmu_works_under_smf table.")
    print()

    mydb.commit()




def modify_DMU(dmu_code, cursor, mydb):

    mycursor = cursor

    money = float(input("Enter money present: "))
    while(check_float_range(money) == False):
        print("Invalid money value. Please enter a valid number.")
        money = float(input("Enter money present: "))

    id_count = int(input("Enter batch id counter: "))
    while(check_float_range(id_count) == False):
        print("Invalid batch id counter value. Please enter a valid number.")
        id_count = int(input("Enter batch id counter: "))

    sql = "UPDATE DMU SET money = %s, batch_id_counter = %s WHERE district_code = %s"
    val = (money, id_count, dmu_code)
    mycursor.execute(sql, val)

    print(mycursor.rowcount, "record(s) affected")
    print()

    mydb.commit()



def select_DMU_In_SMF(smf_code, cursor):

    mycursor = cursor
    query = """SELECT * FROM DMU
                        NATURAL JOIN DMU_Works_Under_SMF
                        WHERE DMU_Works_Under_SMF.state_code = '{SMF}'""".format(SMF = smf_code)
    mycursor.execute(query)
    dmu_data = mycursor.fetchall()

    print()
    print("DMUs available: ", smf_code, sep="")
    print("------------------------------------------------------------")
    print("|DMU Code|")
    print("------------------------------------------------------------")
    count = 1
    for i in dmu_data:
        print(count, ". ", i[0], sep="")
        count += 1
    print(count, ". ", "Back", sep="")
    dfin = int(input("Enter your choice: "))
    while(dfin > len(dmu_data) or dfin < 1):
        print("Invalid DMU. Please enter a valid DMU.")
        dfin = int(input("Enter your choice: "))
    if(dfin!=len(dmu_data)+1):
        dmu_chosen = dmu_data[dfin-1][0]
    else:
        dmu_chosen = None

    return dmu_chosen




def display_DMU(dmu_chosen, cursor):

    mycursor = cursor
    query = "SELECT * FROM DMU WHERE district_code = '{dmu_id}'".format(dmu_id=dmu_chosen)
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    print()
    print("DMU Chosen: ", dmu_chosen, sep="")
    print("--------------------------------------------------------------------------")
    print("District Code\t\tDistrict Name\t\tMoney\t\tBatch ID Counter")
    print("--------------------------------------------------------------------------")
    print(myresult[0][0], "\t\t\t\t\t", myresult[0][1], "\t\t\t", myresult[0][2], "\t\t\t", myresult[0][3], sep="")

    print()
    print()

    return


def delete_DMU(dmu_chosen, cursor, mydb):

    mycursor = cursor

    get_vdcs_code_sql = "SELECT vdcs_code FROM VDCS_Works_Under_DMU WHERE district_code = '{dmu_coder}'".format(dmu_coder=dmu_chosen)
    mycursor.execute(get_vdcs_code_sql)
    vdcs_codes = mycursor.fetchall()
    print(vdcs_codes)

    delete_df_sql = "DELETE FROM Dairy_Farmer WHERE farmer_identification_id = '{fid}'"
    get_aadhar_sql = "SELECT aadhar_card_id FROM Dairy_Farmer_Possesses WHERE farmer_identification_id = '{df_coder}'"
    # print("2")

    for vdcs_code in vdcs_codes:
        get_df_code_sql = "SELECT farmer_identification_id FROM DF_Works_Under_VDCS WHERE vdcs_code = '{vdcs_coder}'".format(vdcs_coder=vdcs_code[0])
        mycursor.execute(get_df_code_sql)
        df_codes = mycursor.fetchall()
        # print(df_codes)

        for df_code in df_codes:
            mycursor.execute(get_aadhar_sql.format(df_coder=df_code[0]))
            aadhar_card_id = mycursor.fetchall()[0][0]
            delete_aa_sql = "DELETE FROM AADHAR_CARD WHERE aadhar_card_id = '{aadhar_number}'".format(aadhar_number=aadhar_card_id)
            mycursor.execute(delete_aa_sql)
            # print("4")

            mycursor.execute(delete_df_sql.format(fid=df_code[0]))

        delete_vdcs_sql = "DELETE FROM VDCS WHERE vdcs_code = '{vdcs_code}'".format(vdcs_code=vdcs_code[0])
        mycursor.execute(delete_vdcs_sql)

    delete_dmu_sql = "DELETE FROM DMU WHERE district_code = '{dmu_code}'".format(dmu_code=dmu_chosen)
    mycursor.execute(delete_dmu_sql)

    print(mycursor.rowcount, "record(s) deleted")
    print()




    mydb.commit()






































