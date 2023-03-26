
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
print()
mycursor = mydb.cursor()




def select_which_trigger():

    flag = 0
    while(flag != 1):

        print("Choose a trigger:")
        print("1. Trigger 1")
        print("2. Trigger 2")
        print("3. Exit")
        print()

        trigger_choice = int(input("Enter your choice: "))
        while(trigger_choice > 3 or trigger_choice < 1):
            print("Invalid trigger. Please enter a valid trigger.")
            trigger_choice = int(input("Enter your choice: "))

        if trigger_choice == 3:
            print("Exiting...")
            flag = 1

        elif trigger_choice == 1:
            trigger1()
        else:
            trigger2()

    return

def select_DMU(dmu_id_list, dmu_name_list):
    print("Choose a DMU:")
    for i in range(1, len(dmu_id_list) + 1):
        print(i, ". ", dmu_name_list[i - 1], sep="")

    print()

    dmu_choice = int(input("Enter your choice: "))
    while(dmu_choice > len(dmu_id_list) or dmu_choice < 1):
        print("Invalid DMU. Please enter a valid DMU.")
        dmu_choice = int(input("Enter your choice: "))

    print("DMU chosen: ", dmu_name_list[dmu_choice - 1], sep="")
    print()

    return dmu_id_list[dmu_choice - 1]

def select_VDCS(dmu_chosen):
    print("Choose a VDCS:")
    query = """SELECT * FROM VDCS
                        NATURAL JOIN VDCS_Works_Under_DMU
                        WHERE VDCS_Works_Under_DMU.district_code = '{DMU}'""".format(DMU = dmu_chosen)
    mycursor.execute(query)
    vdcs_data = mycursor.fetchall()
    vdcs_id_list = [i[0] for i in vdcs_data]
    vdcs_name_list = [i[4] for i in vdcs_data]

    for i in range(1, len(vdcs_id_list) + 1):
        print(i, ". ", vdcs_name_list[i - 1], sep="")

    print()

    vdcs_choice = int(input("Enter your choice: "))
    while(vdcs_choice > len(vdcs_id_list) or vdcs_choice < 1):
        print("Invalid VDCS. Please enter a valid VDCS.")
        vdcs_choice = int(input("Enter your choice: "))

    print("VDCS chosen: ", vdcs_name_list[vdcs_choice - 1], sep="")
    print()

    return vdcs_id_list[vdcs_choice - 1]



def trigger1():

    # store all the data from the Dmu_Transaction table in a list
    mycursor.execute("SELECT * FROM DMU_Transaction")
    dmu_transaction_data = mycursor.fetchall()

    # Extract the transaction id from the list and store it in a list
    transaction_id_list = [i[0] for i in dmu_transaction_data]
    # find the maximum transaction id
    max_transaction_id = max(transaction_id_list)
    int_max_transaction_id = int(max_transaction_id)
    int_max_transaction_id += 1
    # calculate how many digits are there in the maximum transaction id
    digits = len(str(int_max_transaction_id))
    # add 0s to the front of the maximum transaction id to make it 10 digits long
    new_transaction_id = "0" * (10 - digits) + str(int_max_transaction_id)


    mycursor.execute("SELECT * FROM DMU")
    dmu_data = mycursor.fetchall()

    # Extract the dmu id from the list and store it in a list
    dmu_id_list = [i[0] for i in dmu_data]
    # Extract the dmu name from the list and store it in a list
    dmu_name_list = [i[1] for i in dmu_data]

    dmu_chosen = select_DMU(dmu_id_list, dmu_name_list)
    vdcs_chosen = select_VDCS(dmu_chosen)

    money_available = 0
    # set the money available to the money available in the DMU chosen
    for i in dmu_data:
        if i[0] == dmu_chosen:
            money_available = i[2]

    amount_sent = float(input("Enter the amount to be sent: "))
    while(amount_sent > 999999999999.99 or amount_sent < 0):
        print("Invalid amount. Please enter a valid amount.")
        amount_sent = float(input("Enter the amount to be sent: "))
    print()


    query = """INSERT INTO DMU_Transaction (t_id, district_code, vdcs_code, amount_sent) VALUES (%s, %s, %s, %s)"""
    values = (new_transaction_id, dmu_chosen, vdcs_chosen, amount_sent)
    try:
        mycursor.execute(query, values)
    except:
        print("Error in inserting data.")
        
    mydb.commit()

    # print how many rows were affected
    print(mycursor.rowcount, "record(s) inserted.")
    print()






def trigger2():
    # store all the data from the Dairy_Farmer table in a list
    mycursor.execute("SELECT * FROM Dairy_Farmer")
    dairy_data = mycursor.fetchall()

    # Extract the farmer id from the list and store it in a list
    dairy_id_list = [i[0] for i in dairy_data]

    dairy_delete = input("Enter the id of the dairy farmer to be deleted: ")
    while(dairy_delete not in dairy_id_list):
        print("Invalid ID. Please enter a valid ID.")
        dairy_delete = input("Enter the id of the dairy farmer to be deleted: ")
    print()

    query = """DELETE FROM Dairy_Farmer WHERE farmer_identification_id=%s"""
    mycursor.execute(query, (dairy_delete,))
    mydb.commit()

    # print how many rows were affected
    print(mycursor.rowcount, "record(s) after deleteion.")
    print()





if __name__ == "__main__":
    select_which_trigger()
