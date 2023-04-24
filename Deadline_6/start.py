import mysql.connector
from insert_df import *
from insert_vdcs import *
from insert_dmu import *
from insert_smf import *
from check_float import *




def select_SMF(mycursor):
    query = """SELECT * FROM SMF"""
    mycursor.execute(query)
    smf_data = mycursor.fetchall()
    smf_list = [i[0] for i in smf_data]
    print("Choose a SMF:")
    for i in range(len(smf_list)):
        print(i + 1, ". ", smf_list[i], sep="")
    print(len(smf_list) + 1, ". Back", sep="")
    print()

    smfin = int(input("Enter your choice: "))
    while (smfin > len(smf_list)+1 or smfin < 1):
        print("Invalid SMF. Please enter a valid DMU.")
        smfin = int(input("Enter your choice: "))
    if(smfin!=len(smf_list)+1):
        smf_chosen = smf_list[smfin - 1]
    else:
        smf_chosen=None
    return smf_chosen


def select_DMU(mycursor):
    query = """SELECT * FROM DMU"""
    mycursor.execute(query)
    dmu_data = mycursor.fetchall()
    dmu_list = [i[0] for i in dmu_data]
    print("Choose a DMU:")
    for i in range(len(dmu_list)):
        print(i + 1, ". ", dmu_list[i], sep="")
    print(len(dmu_list) + 1, ". Back", sep="")
    print()

    dmuin = int(input("Enter your choice: "))
    while (dmuin > len(dmu_list)+1 or dmuin < 1):
        print("Invalid DMU. Please enter a valid DMU.")
        dmuin = int(input("Enter your choice: "))
    if(dmuin!=len(dmu_list)+1):
        dmu_chosen = dmu_list[dmuin - 1]
    else:
        dmu_chosen=None
    return dmu_chosen


def select_VDCS(mycursor):
    query = """SELECT * FROM VDCS"""
    mycursor.execute(query)
    vdcs_data = mycursor.fetchall()
    vdcs_list = [i[0] for i in vdcs_data]
    print("Choose a VDCS:")
    for i in range(len(vdcs_list)):
        print(i + 1, ". ", vdcs_list[i], sep="")
    print(len(vdcs_list) + 1, ". Back", sep="")
    print()

    vdcsin = int(input("Enter your choice: "))
    while (vdcsin > len(vdcs_list)+1 or vdcsin < 1):
        print("Invalid VDCS. Please enter a valid VDCS.")
        vdcsin = int(input("Enter your choice: "))
    if(vdcsin!=len(vdcs_list)+1):
        vdcs_chosen = vdcs_list[vdcsin - 1]
    else:
        vdcs_chosen=None
    return vdcs_chosen


def select_DF(mycursor):
    query = """SELECT * FROM Dairy_Farmer"""
    mycursor.execute(query)
    df_data = mycursor.fetchall()
    df_list = [i[0] for i in df_data]
    print("Choose a Dairy Farmer:")
    for i in range(len(df_list)):
        print(i + 1, ". ", df_list[i], sep="")
    print(len(df_list) + 1, ". Back", sep="")
    print()

    dfin = int(input("Enter your choice: "))
    while (dfin > len(df_list)+1 or dfin < 1):
        print("Invalid Dairy Farmer. Please enter a valid Dairy Farmer.")
        dfin = int(input("Enter your choice: "))
    if(dfin!=len(df_list)+1):
        df_chosen = df_list[dfin - 1]
    else:
        df_chosen=None

    return df_chosen


def start_SMF(data,mycursor,mydb):
    query = """SELECT * FROM SMF
                                 WHERE state_code = '{SMF}'""".format(SMF = data)
    mycursor.execute(query)
    smf_chosen_data = mycursor.fetchall()
    print("SMF chosen: ", smf_chosen_data[0][1], sep="")
    print("------------------------------------------------------------")
    print("|Code|\t\t|Name|\t\t|Sold|\t\t|Cost|")
    print("------------------------------------------------------------")
    print(smf_chosen_data[0][0], "\t", smf_chosen_data[0][1], "\t", smf_chosen_data[0][2], "\t", smf_chosen_data[0][3])
    print()
    print()

    option = 0
    while (option != 10):
        print("1. Display DMU")
        print("2. Add DMU")
        print("3. Delete DMU")
        print("4. Modify DMU")
        print("5. Display VDCS")
        print("6. Add VDCS")
        print("7. Delete VDCS")
        print("8. Modify VDCS")
        print("9. Display DF")
        print("10. Add DF")
        print("11. Delete DF")
        print("12. Modify DF")
        print("13. Modify SMF")
        print("14. Run Transactions")
        print("15. Back")
        print()
        option = int(input("Enter your choice: "))
        while (option > 15 or option < 1):
            print("Invalid option. Please enter a valid option.")
            option = int(input("Enter your choice: "))
        print()
        if (option == 1):
            dmu_chosen = select_DMU_In_SMF(data,mycursor)
            display_DMU(dmu_chosen, mycursor)

        elif (option == 2):
            insert_DMU(data,mycursor, mydb)

        elif (option == 3):
            dmu_chosen = select_DMU_In_SMF(data,mycursor)
            if(dmu_chosen!=None):
                delete_DMU(dmu_chosen, mycursor, mydb)

        elif (option == 4):
            dmu_chosen = select_DMU_In_SMF(data,mycursor)
            if(dmu_chosen!=None):
                modify_DMU(dmu_chosen, mycursor, mydb)


        elif (option == 5):
            dmu_chosen = select_DMU_In_SMF(data,mycursor)
            if(dmu_chosen!=None):
                vdcs_chosen = select_VDCS_In_DMU(dmu_chosen,mycursor)
                if(vdcs_chosen!=None):
                    display_VDCS(vdcs_chosen, mycursor)


        elif (option == 6):
            dmu_chosen = select_DMU_In_SMF(data,mycursor)
            if(dmu_chosen!=None):
                insert_VDCS(dmu_chosen,mycursor, mydb)


        elif (option == 7):
            dmu_chosen = select_DMU_In_SMF(data,mycursor)
            if(dmu_chosen!=None):
                vdcs_chosen = select_VDCS_In_DMU(dmu_chosen,mycursor)
                if(vdcs_chosen!=None):
                    delete_VDCS(vdcs_chosen, mycursor, mydb)


        elif (option == 8):
            dmu_chosen = select_DMU_In_SMF(data,mycursor)
            if(dmu_chosen!=None):
                vdcs_chosen = select_VDCS_In_DMU(dmu_chosen,mycursor)
                if(vdcs_chosen!=None):
                    modify_VDCS(vdcs_chosen, mycursor, mydb)

        elif (option == 9):
            dmu_chosen = select_DMU_In_SMF(data,mycursor)
            if(dmu_chosen!=None):
                vdcs_chosen = select_VDCS_In_DMU(dmu_chosen,mycursor)
                if(vdcs_chosen!=None):
                    df_chosen = select_DF_In_VDCS(vdcs_chosen,mycursor)
                    if(df_chosen!=None):
                        display_DF(df_chosen, mycursor)


        elif (option == 10):
            dmu_chosen = select_DMU_In_SMF(data,mycursor)
            if(dmu_chosen!=None):
                vdcs_chosen = select_VDCS_In_DMU(dmu_chosen,mycursor)
                if(vdcs_chosen!=None):
                    query = """SELECT village_name FROM VDCS WHERE vdcs_code = '{VDCS}'""".format(VDCS = vdcs_chosen)
                    mycursor.execute(query)
                    village_name = mycursor.fetchall()
                    # print(village_name)
                    insert_DF(vdcs_chosen,village_name[0][0],mycursor, mydb)

        elif (option == 11):
            dmu_chosen = select_DMU_In_SMF(data,mycursor)
            if(dmu_chosen!=None):
                vdcs_chosen = select_VDCS_In_DMU(dmu_chosen,mycursor)
                if(vdcs_chosen!=None):
                    df_chosen = select_DF_In_VDCS(vdcs_chosen,mycursor)
                    if(df_chosen!=None):
                        delete_DF(df_chosen, mycursor, mydb)

        elif (option == 12):
            dmu_chosen = select_DMU_In_SMF(data,mycursor)
            if(dmu_chosen!=None):
                vdcs_chosen = select_VDCS_In_DMU(dmu_chosen,mycursor)
                if(vdcs_chosen!=None):
                    df_chosen = select_DF_In_VDCS(vdcs_chosen,mycursor)
                    if(df_chosen!=None):
                        modify_DF(df_chosen, mycursor, mydb)


        elif (option == 13):
            modify_SMF(data,mycursor, mydb)

        elif(option==14):
            run_transactions(data,mycursor,mydb)

        elif (option == 15):
            break



    """Display DMU/VDCS/DF
    Add DMU/VDCS/DF
    Delete DMU/VDCS/DF
    Modify SMF/DMU/VDCS/DF
    Run Transactions"""


def start_DMU(data,mycursor,mydb):
    query = """SELECT * FROM DMU
                     WHERE district_code = '{DMU}'""".format(DMU = data)
    mycursor.execute(query)
    dmu_data = mycursor.fetchall()
    print("DMU chosen: ", dmu_data[0][1], sep="")
    print("--------------------------------------------------------------")
    print("|Code|\t\t|Name|\t|Money|\t\t|Batch_Counter|\t|State Code|")
    print("--------------------------------------------------------------")
    print(dmu_data[0][0], "\t\t", dmu_data[0][1], "\t", dmu_data[0][2], "\t\t",
          dmu_data[0][3], "\t\t\t", dmu_data[0][0][:3])
    print()
    print()

    option = 0
    while (option != 10):
        print("Choose an option:")
        print("1. Display VDCS")
        print("2. Add VDCS")
        print("3. Delete VDCS")
        print("4. Modify VDCS")
        print("5. Display DF")
        print("6. Add DF")
        print("7. Delete DF")
        print("8. Modify DF")
        print("9. Modify DMU")
        print("10. Back")
        print()
        option = int(input("Enter your choice: "))
        while (option > 10 or option < 1):
            print("Invalid option. Please enter a valid option.")
            option = int(input("Enter your choice: "))
        if (option == 1):
            vdcs_chosen = select_VDCS_In_DMU(data,mycursor)
            if(vdcs_chosen!=None):
                display_VDCS(vdcs_chosen,mycursor)

        elif (option == 2):
            insert_VDCS(data,mycursor,mydb)

        elif (option == 3):
            vdcs_chosen = select_VDCS_In_DMU(data,mycursor)
            if(vdcs_chosen!=None):
                delete_VDCS(vdcs_chosen,mycursor,mydb)

        elif (option == 4):
            vdcs_chosen = select_VDCS_In_DMU(data, mycursor)
            if (vdcs_chosen != None):
                modify_VDCS(vdcs_chosen, mycursor, mydb)

        elif (option == 5):
            vdcs_chosen = select_VDCS_In_DMU(data, mycursor)
            if (vdcs_chosen != None):
                display_DF(select_DF_In_VDCS(vdcs_chosen, mycursor), mycursor)

        elif (option == 6):
            vdcs_chosen = select_VDCS_In_DMU(data, mycursor)
            if (vdcs_chosen != None):
                query = """SELECT village_name FROM VDCS WHERE vdcs_code = '{VDCS}'""".format(VDCS=vdcs_chosen)
                mycursor.execute(query)
                village_name = mycursor.fetchall()
                # print(village_name)
                insert_DF(vdcs_chosen, village_name[0][0], mycursor, mydb)


        elif (option == 7):
            vdcs_chosen = select_VDCS_In_DMU(data, mycursor)
            if (vdcs_chosen != None):
                delete_DF(select_DF_In_VDCS(vdcs_chosen, mycursor), mycursor, mydb)


        elif (option == 8):
            vdcs_chosen = select_VDCS_In_DMU(data, mycursor)
            if (vdcs_chosen != None):
                modify_DF(select_DF_In_VDCS(vdcs_chosen, mycursor), mycursor, mydb)

        elif (option == 9):
            modify_DMU(data, mycursor, mydb)

        elif (option == 10):
            break

    print()
    print()


    """Display VDCS/DF
    Add VDCS/DF
    Delete VDCS/DF
    Modify DMU/VDCS/DF"""

def start_VDCS(data,mycursor,mydb):
    query = """SELECT * FROM VDCS
                        WHERE vdcs_code = '{VDCS}'""".format(VDCS = data)
    mycursor.execute(query)
    vdcs_data = mycursor.fetchall()
    print("VDCS chosen: ", vdcs_data[0][4], sep="")
    print("----------------------------------------------------------------------------------")
    print("|VDCS Code|\t |Cattlefeed|\t |Money|\t\t|Milk Quantity|\t\t |Village Name|")
    print("----------------------------------------------------------------------------------")
    print(vdcs_data[0][0], "\t\t\t", vdcs_data[0][1], "\t\t\t", vdcs_data[0][2], "\t\t\t",
          vdcs_data[0][3], "\t\t\t", vdcs_data[0][4])
    print()
    print()

    option = 0

    while (option != 6):
        print("Choose an option:")
        print("1. Display DF")
        print("2. Add DF")
        print("3. Delete DF")
        print("4. Modify DF")
        print("5. Modify VDCS")
        print("6. Back")
        print()
        option = int(input("Enter your choice: "))
        while (option > 6 or option < 1):
            print("Invalid option. Please enter a valid option.")
            option = int(input("Enter your choice: "))
        if (option == 6):
            break
        elif (option == 1):
            df_chosen = select_DF_In_VDCS(data,mycursor)
            if(df_chosen!=None):
                display_DF(df_chosen,mycursor)

        elif (option == 2):
            insert_DF(data,vdcs_data[0][4],mycursor,mydb)

        elif (option == 3):
            df_chosen = select_DF_In_VDCS(data,mycursor)
            if(df_chosen!=None):
                delete_DF(df_chosen,mycursor,mydb)


        elif (option == 4):
            df_chosen = select_DF_In_VDCS(data,mycursor)
            if(df_chosen!=None):
                modify_DF(df_chosen,mycursor,mydb)

        elif (option == 5):
            vdcs_chosen = data
            if(vdcs_chosen!=None):
                modify_VDCS(vdcs_chosen,mycursor,mydb)

        else:
            print("Invalid option. Please enter a valid option.")

    """Display DF
    Add DF
    Delete DF
    Modify VDCS/DF"""


def start_DF(data,mycursor,mydb):
    df_chosen = data
    query = """SELECT * FROM Dairy_Farmer
                        WHERE farmer_identification_id = '{F_id}'""".format(F_id = data)
    mycursor.execute(query)
    dairy_farmer_data = mycursor.fetchall()
    print("Dairy Farmer chosen: ", dairy_farmer_data[0][0], sep="")
    print("------------------------------------------------------------")
    print("|DF Code|\t|Milk Quantity|\t|Avg Milk Qty|\t|Cattle Feed|")
    print("------------------------------------------------------------")
    print(dairy_farmer_data[0][0], "\t\t", dairy_farmer_data[0][1], "\t\t\t",
          dairy_farmer_data[0][2], "\t\t\t", dairy_farmer_data[0][3])
    print()
    print()
    option = 0
    while(option!=3):
        print()
        print("1. Modify details")
        print("2. View Aadhar Details")
        print("3. Back")
        option = int(input("Enter your choice: "))
        while (option > 3 or option < 1):
            print("Invalid choice. Please enter a valid choice.")
            option = int(input("Enter your choice: "))
        if(option==1):
            modify_DF(df_chosen,mycursor,mydb)
        elif(option==2):
            view_aadhar_details(df_chosen,mycursor)
        else:
            break

    """Modify DF"""


def select_account(mycursor):
    flag = 0
    while(flag != 1):
        print("Choose which type of account you want to enter in:")
        print("1. SMF account")
        print("2. DMU account")
        print("3. VDCS account")
        print("4. DF account")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        print()

        while (choice > 5 or choice < 1):
            print("Invalid choice. Please enter a valid choice.")
            choice = int(input("Enter your choice: "))
            print()

        if choice == 1:
            ans=select_SMF(mycursor)
            if(ans!=None):
                return (1,ans)
            else:
                return (5,None)
        elif choice == 2:
            ans=select_DMU(mycursor)
            if(ans!=None):
                return (2,ans)
            else:
                return (5,None)
        elif choice == 3:
            ans=select_VDCS(mycursor)
            if(ans!=None):
                return (3,ans)
            else:
                return (5,None)
        elif choice == 4:
            ans=select_DF(mycursor)
            if(ans!=None):
                return (4,ans)
            else:
                return (5,None)
        else:
            return (None,None)

if __name__ == "__main__":
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="farhan",
            database="All_Levels"
        )
        print("Connected to the database.")
        print()
        mycursor = mydb.cursor()
        type=5
        while(type==5):
            type,data=select_account(mycursor)
            if(type==1):
                start_SMF(data,mycursor,mydb)
            elif(type==2):
                start_DMU(data,mycursor,mydb)
            elif(type==3):
                start_VDCS(data,mycursor,mydb)
            elif(type==4):
                start_DF(data,mycursor,mydb)

        #close the connection
        mydb.commit()
        mydb.close()
    except:
        print("Connection failed.")
        print("Exiting...")
        exit()

    print("Thank you for using the system. Have a nice day!")
