import sqlite3
import os


def choice_4():
    connection = sqlite3.connect('SubAgentAccount.db')
    cursor = connection.cursor()
    not_fund = True
    choice = True
    while choice:
        not_fund = True
        #os.system('cls')
        print()
        print()
        print()
        pp_no = input('   Enter Passport Number :- ')

        if pp_no == "0":
            break
        select_all_record = """select * from PassportHm"""
        cursor.execute(select_all_record)
        records = cursor.fetchall()

        for row in records:
            if row[0] == pp_no:
                print('   Passport Number :- ', row[0])
                print("   Housemaid's name :- ", row[1])
                wait_1 = input('   Already this code is exits...Pls press enter key !')
                not_fund = False

        if not_fund:
            HmName = input("   Housemaid's Name :- ")
            Com = int(input('   Commission :- '))
            select_all_record_sub_agent = """select * from SubAgent"""
            cursor.execute((select_all_record_sub_agent))
            records_sub_agent = cursor.fetchall()
            sub_id = int(input('  Enter Sub-agent Code :- '))
            print()
            for row in records_sub_agent:
                if row[0] == sub_id:
                    name = row[1]
            print('  Sub Agent Name :- ', name)
            sav = input('   Do you want to Save this (Y/N)? ')
            if sav == 'Y':
                insert_record = """INSERT INTO PassportHm (PassportNo, Name, Comm, sub_id, sub_name) VALUES (?, ?, ?, ?, ?);"""
                data = (pp_no, HmName, Com, sub_id, name)
                cursor.execute(insert_record, data)
                connection.commit()

    cursor.close()


