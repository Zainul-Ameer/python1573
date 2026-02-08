

def choice_12():

    import sqlite3
    import os

    connection = sqlite3.connect('SubAgentAccount.db')
    cursor = connection.cursor()
    os.system('cls')
    print()
    print()
    select_all_record = """select * from SubAgentDetails"""
    cursor.execute(select_all_record)
    records1 = cursor.fetchall()
    code = input('   Enter Date :- ')
    os.system('cls')
    print('')
    print('')
    print('   ---  ACCOUNT DETAILS  ---')
    total = 0
    print()
    print()
    print('   Date :- ', code)
    for row in records1:
        if row[2] == code:
            des = row[5]
            a5 = len(row[5])
            b5 = 50
            c5 = b5 - a5
            print()
            print('   Sub Agent Name   :- ', row[1])
            print("   Housemaid's Name :- ", row[4])
            print('   Description      :- ', row[5])
            print("   Amount           :-  Rs. {:,.2f}".format(row[6]))






            total = total + row[6]


    print()
    print("    Total Outstanding Amount :- Rs. {:,.2f}".format(total))
    print()
    press_key = input('      Press Enter Key to coutinue......')


