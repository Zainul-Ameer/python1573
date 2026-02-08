import sqlite3
import os
connection = sqlite3.connect('SubAgentAccount.db')
cursor = connection.cursor()


select_all_record = """select * from SubAgent"""
cursor.execute(select_all_record)
records = cursor.fetchall()
id = int(input('Enter the id number :- '))
ppNumber = input('Enter Passport Number :- ')
os.system('cls')
print()
print()
for row in records:
    if row[0] == id:
        print(f"   Customer's Code : {row[0]}   Customer's Name :- {row[1]}")


select_all_record = """select * from SubAgentDetails"""
cursor.execute(select_all_record)
records1 = cursor.fetchall()
total = 0
for row in records1:
    if row[3] == ppNumber:
        print(f'   Passport No.:- {row[3]}    Housemaid Name :- {row[4]}')
        print('')
        print('')
        break
#print('   Date    Passport No.   Name              Description       Amount')
for row1 in records1:
    if row1[0] == id and row1[3] == ppNumber:

        print("   Date :- ", row1[2])
        print('   Description :- ', row1[5])
        print('   Amount :- Rs. {:,.2f}'.format(row1[6]))
        #print('  Balance :- Rs {:,.2f}'.format(customer_balance[new]))


        print()

        total = total + row1[6]


cursor.close()
print("   Total Amount :- Rs {:,.2f}".format(total))