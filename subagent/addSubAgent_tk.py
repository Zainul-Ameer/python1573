import sqlite3
import os

"""
def choice_1():
    connection = sqlite3.connect('SubAgentAccount.db')
    cursor = connection.cursor()

    select_all_record = """select * from SubAgent"""
    cursor.execute(select_all_record)
    records = cursor.fetchall()
    not_fund = True
    choice = True

    while choice:
        not_fund = True
        #os.system('cls')
        print()
        print()
        print()
        id_num = int(input('   Enter the id number :- '))

        if id_num == 0:
            break
        select_all_record = """select * from SubAgent"""
        cursor.execute(select_all_record)
        records = cursor.fetchall()

        for row in records:
            if row[0] == id_num:
                print('   Customer I.D   :- ', row[0])
                print("   Customer's name :- ", row[1])
                wait_1 = input('   Already this code is exits...Pls press enter key !')
                not_fund = False

        if not_fund:
            subName = input('   Sub Agent Name :- ')
            print()
            sav = input('   Do you want to Save this (Y/N)? ')
            if sav == 'Y':
                insert_record = """INSERT INTO SubAgent (id, Name) VALUES (?, ?);"""
                data = (id_num, subName)
                cursor.execute(insert_record, data)
                connection.commit()

    cursor.close()

choice_1()
    
"""