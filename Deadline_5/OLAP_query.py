
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


OLAP_query1 = """SELECT district_code as District,R.X as Village, R.Y as Money, RANK() OVER (PARTITION BY district_code ORDER BY R.Y DESC) as RANK_Money FROM (SELECT VDCS.VDCS_code as X,district_code, SUM(amount_sent) as Y FROM VDCS NATURAL JOIN DMU_TRANSACTION NATURAL JOIN VDCS_Works_Under_DMU GROUP BY VDCS.VDCS_code,district_code) as R"""
OLAP_query2 = """SELECT R.X as District, R.Y as Money, PERCENT_RANK() OVER (ORDER BY R.Y DESC) as PER_RANK_Money, CUME_DIST() OVER (ORDER BY R.Y DESC) as CUM_DIST_Money FROM (SELECT DMU.district_code as X, SUM(amount_sent) as Y FROM DMU NATURAL JOIN SMF_TRANSACTION GROUP BY district_code) as R"""
OLAP_query3 = """SELECT district_code,vdcs_code,sex,COUNT(*) AS count FROM (SELECT farmer_identification_id,sex FROM AADHAR_CARD NATURAL JOIN Dairy_Farmer_Possesses) as A NATURAL JOIN DF_Works_Under_VDCS NATURAL JOIN VDCS_Works_Under_DMU GROUP BY district_code,vdcs_code,sex WITH ROLLUP"""
OLAP_query4 = """SELECT R.retailer_id as 'Retailer ID', R.retailer_name as 'Retailer_Name', R.district_code as 'District Code', R.amount_bought as 'Amount Bought',AVG(R.amount_bought) OVER (PARTITION BY R.district_code ORDER BY R.amount_bought ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) as 'Average Amount Bought' FROM Retailers as R;"""

OLAP_query1_header = ["|District|", "|Village|", "|Money|", "|RANK_Money|"]
OLAP_query2_header = ["|District|", "|Money|", "|PER_RANK_Money|", "|CUM_DIST_Money|"]
OLAP_query3_header = ["|District_Code|","|VDCS_Code|","|Sex|","|Count|"]
OLAP_query4_header = ["|Retailer_ID|", "|Retailer_Name|", "|District_Code|", "|Amount_Bought|", "|Average_Amount_Bought|"]


def choose_query(query_number):
    if query_number == 1:
        return OLAP_query1,OLAP_query1_header
    elif query_number == 2:
        return OLAP_query2,OLAP_query2_header
    elif query_number == 3:
        return OLAP_query3,OLAP_query3_header
    elif query_number == 4:
        return OLAP_query4,OLAP_query4_header
    else:
        return "Invalid query number"

def display_OLAP_options():
    flag = 0
    while(flag != 1):
        print("Choose an OLAP query:")
        print("1. Display the ranking of the VDCSes in a district in terms of the most money received from their respective DMUs")
        print("2. Display the percentage rank and cumulative distribution of the DMUs in terms of the most money received from their respective SMFs")
        print("3. Display the total number of farmers district-wise, village-wise and sex-wise and include the total counts for each level")
        print("4. Display the average money spent by the retailers in different districts among the retailers that are the closest to its own amount spent")
        print("5. Exit")
        print()
        query_number = int(input("Enter your choice: "))
        while (query_number > 5 or query_number < 1):
            print("Invalid query number. Please enter a valid query number.")
            query_number = int(input("Enter your choice: "))

        if query_number == 5:
            flag = 1
        else:
            query,header = choose_query(query_number)
            mycursor.execute(query)
            result = mycursor.fetchall()
            print()
            print("Result:")
            print()
            print("---------------------------------------------------------------------------------------------")
            for col in header:
                print(col, end = "\t")
            print()
            print("---------------------------------------------------------------------------------------------")

            for row in result:
                for col in row:
                    print(col, end = "\t\t")
                print()
            print()
            print()



if __name__ == "__main__":
    display_OLAP_options()

    print("Exiting...")
    exit()



