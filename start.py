import mysql.connector
from insert_df import df_seetry
from insert_smf import smf_seetry
from insert_dmu import dmu_seetry
from insert_vdcs import vdcs_seetry


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
                start_SMF(data,mycursor)
            elif(type==2):
                start_DMU(data,mycursor)
            elif(type==3):
                start_VDCS(data,mycursor)
            elif(type==4):
                start_DF(data,mycursor)
        #close the connection  
        mydb.close()
    except:
        print("Connection failed.")
        print("Exiting...")
        exit()

    print("Thank you for using the system. Have a nice day!")


