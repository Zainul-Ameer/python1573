import datetime
import sqlite3
connection = sqlite3.connect('SubAgentAccount.db')
cursor = connection.cursor()

select_all_record = """select * from SubAgent"""
cursor.execute(select_all_record)
records = cursor.fetchall()

x = datetime.datetime.now()
today_date = (x.strftime("%x"))
print('   Date :- ', today_date)
id = int(input('   Enter the Customer Code :- '))
for row in records:
    if row[0] == id:
        subName = row[1]
        print("   Customer's Name :- ", row[1])
        housePassportNumber = input("   Housemaid's Passport Number :-")
        houseName = input("   Housemaid's Name :-")
        des = input("   Description :- ")
        amu = int(input("   Amount      :- "))
        dep = 0

        insert_record = """INSERT INTO SubAgentDetails 
        (SubId, SubName, DateCash, HousemaidPP, HousemaidName, Description, Credit, Depit) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
        data = (id, subName, today_date,  housePassportNumber, houseName, des, amu, dep)
        cursor.execute(insert_record, data)
        connection.commit()
        cursor.close()