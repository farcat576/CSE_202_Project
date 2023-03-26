
import mysql.connector
from embedded_query2 import seetry


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


state_dict = {1:"GUJ", 2:"EXIT"}
state_name_dict = {1:"Gujarat", 2:"Exit"}




def select_SMF():
    flag = 0
    while(flag != 1):
        print("Choose an SMF:")
        for i in range(1, len(state_dict) + 1):
            print(i, ". ", state_name_dict[i], sep="")

        print()

        smfin = int(input("Enter your choice: "))
        while (smfin > 2 or smfin < 1):
            print("Invalid SMF. Please enter a valid SMF.")
            smfin = int(input("Enter your choice: "))

        if(smfin == 2):
            flag = 1
        else:
            SMF_details(state_dict[smfin])

    return


def SMF_details(smf_chosen):

    query = """SELECT * FROM SMF
                             WHERE state_code = '{SMF}'""".format(SMF = smf_chosen)
    mycursor.execute(query)
    smf_chosen_data = mycursor.fetchall()
    print("SMF chosen: ", smf_chosen_data[0][1], sep="")
    print("------------------------------------------------------------")
    print("|Code|\t\t|Name|\t\t|Sold|\t\t|Cost|")
    print("------------------------------------------------------------")
    print(smf_chosen_data[0][0], "\t", smf_chosen_data[0][1], "\t", smf_chosen_data[0][2], "\t", smf_chosen_data[0][3])
    print()
    print()

    dmu_data = display_DMUs(smf_chosen_data[0][0])
    dmu_list = [i[0] for i in dmu_data]
    dmuin = select_DMU(dmu_list)
    if(dmuin == len(dmu_list) + 1):
        pass
    else:
        dmu_chosen = dmu_list[dmuin - 1]
        DMU_details(dmuin, dmu_chosen, dmu_data)

    return




def display_DMUs(smf_chosen):
    print("|DMUs available|")
    query = """SELECT * FROM DMU
                     NATURAL JOIN DMU_Works_Under_SMF
                     WHERE DMU_Works_Under_SMF.state_code = '{SMF}'""".format(SMF = smf_chosen)
    mycursor.execute(query)
    dmu_data = mycursor.fetchall()

    return dmu_data

def select_DMU(dmu_list):
    print("Choose a DMU:")
    for i in range(len(dmu_list)):
        print(i + 1, ". ", dmu_list[i], sep="")
    print(len(dmu_list) + 1, ". Back", sep="")
    print()

    dmuin = int(input("Enter your choice: "))
    while (dmuin > len(dmu_list)+1 or dmuin < 1):
        print("Invalid DMU. Please enter a valid DMU.")
        dmuin = int(input("Enter your choice: "))

    return dmuin


def DMU_details(dmuin,dmu_chosen,dmu_data):
    flag = 0
    while(flag!= 1):
        print("DMU chosen: ", dmu_chosen, sep="")
        print("--------------------------------------------------------------")
        print("|Code|\t\t|Name|\t|Money|\t\t|Batch_Counter|\t|State Code|")
        print("--------------------------------------------------------------")
        print(dmu_data[dmuin - 1][0], "\t\t", dmu_data[dmuin - 1][1], "\t", dmu_data[dmuin - 1][2], "\t\t",
              dmu_data[dmuin - 1][3], "\t\t\t", dmu_data[dmuin - 1][4])
        print()
        print()

        vdcs_data = display_VDCSs(dmu_chosen)
        vdcs_list = [i[0] for i in vdcs_data]

        vdcsin = select_VDCS(vdcs_list)
        if(vdcsin == len(vdcs_list) + 1):
            flag = 1
        else:
            vdcs_chosen = vdcs_list[vdcsin - 1]
            VDCS_details(vdcsin, vdcs_chosen, vdcs_data)




def display_VDCSs(dmu_chosen):
    print("|VDCS available|")
    query = """SELECT * FROM VDCS
                        NATURAL JOIN VDCS_Works_Under_DMU
                        WHERE VDCS_Works_Under_DMU.district_code = '{DMU}'""".format(DMU = dmu_chosen)
    mycursor.execute(query)
    vdcs_data = mycursor.fetchall()

    return vdcs_data


def select_VDCS(vdcs_list):
    print("Choose a VDCS:")
    for i in range(len(vdcs_list)):
        print(i + 1, ". ", vdcs_list[i], sep="")
    print(len(vdcs_list) + 1, ". Back", sep="")
    print()

    vdcsin = int(input("Enter your choice: "))
    while (vdcsin > len(vdcs_list)+1 or vdcsin < 1):
        print("Invalid VDCS. Please enter a valid VDCS.")
        vdcsin = int(input("Enter your choice: "))

    return vdcsin


def VDCS_details(vdcsin,vdcs_chosen,vdcs_data):
    flag = 0
    while(flag != 1):
        print("VDCS chosen: ", vdcs_chosen, sep="")
        print("----------------------------------------------------------------------------------")
        print("|VDCS Code|\t |Cattlefeed|\t |Money|\t\t|Milk Quantity|\t\t |Village Name|")
        print("----------------------------------------------------------------------------------")
        print(vdcs_data[vdcsin - 1][0], "\t\t\t", vdcs_data[vdcsin - 1][1], "\t\t\t", vdcs_data[vdcsin - 1][2], "\t\t\t",
              vdcs_data[vdcsin - 1][3], "\t\t\t", vdcs_data[vdcsin - 1][4])
        print()
        print()

        dairy_farmer_data = display_Dairy_Farmers(vdcs_chosen)
        dairy_farmer_list = [i[0] for i in dairy_farmer_data]

        dairy_farmerin = select_Dairy_Farmer(dairy_farmer_list)
        if(dairy_farmerin == len(dairy_farmer_list) + 1):
            flag = 1
        else:
            dairy_farmer_chosen = dairy_farmer_list[dairy_farmerin - 1]
            Dairy_Farmer_details(dairy_farmerin, dairy_farmer_chosen, dairy_farmer_data)




def display_Dairy_Farmers(vdcs_chosen):
    print("Dairy Farmers available:")
    query = """SELECT * FROM Dairy_Farmer
                        NATURAL JOIN DF_Works_Under_VDCS
                        WHERE DF_Works_Under_VDCS.vdcs_code = '{VDCS}'""".format(VDCS = vdcs_chosen)
    mycursor.execute(query)
    dairy_farmer_data = mycursor.fetchall()

    return dairy_farmer_data


def select_Dairy_Farmer(dairy_farmer_list):
    print("Choose a Dairy Farmer:")
    for i in range(len(dairy_farmer_list)):
        print(i + 1, ". ", dairy_farmer_list[i], sep="")
    print(len(dairy_farmer_list) + 1, ". Back", sep="")
    dairy_farmerin = int(input("Enter your choice: "))
    print()

    while (dairy_farmerin > len(dairy_farmer_list)+1 or dairy_farmerin < 1):
        print("Invalid Dairy Farmer. Please enter a valid Dairy Farmer.")
        dairy_farmerin = int(input("Enter your choice: "))

    return dairy_farmerin


def Dairy_Farmer_details(dairy_farmerin,dairy_farmer_chosen,dairy_farmer_data):
    print("Dairy Farmer chosen: ", dairy_farmer_chosen, sep="")
    print("------------------------------------------------------------")
    print("|DF Code|\t|Milk Quantity|\t|Milk Price|\t|Village Name|")
    print("------------------------------------------------------------")
    print(dairy_farmer_data[dairy_farmerin - 1][0], "\t\t", dairy_farmer_data[dairy_farmerin - 1][1], "\t\t\t",
          dairy_farmer_data[dairy_farmerin - 1][2], "\t\t\t", dairy_farmer_data[dairy_farmerin - 1][3])
    print()
    print()


def select_which_embedded_query():
    flag = 0
    while(flag != 1):
        print("Choose which type of embedded query you want to run:")
        print("1. View data")
        print("2. Insert data")
        print("3. Exit")
        print()

        choice = int(input("Enter your choice: "))
        print()

        while (choice > 3 or choice < 1):
            print("Invalid choice. Please enter a valid choice.")
            choice = int(input("Enter your choice: "))
            print()

        if choice == 1:
            select_SMF()
        elif choice == 2:
            seetry()
        else:
            flag = 1



if __name__ == "__main__":

    select_which_embedded_query()

    # close the connection
    mydb.close()

    print("Thank you for using the system. Have a nice day!")



