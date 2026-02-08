import datetime
import os
x = datetime.datetime.now()
dat = (x.strftime("%x"))
os.system('cls')


def choice_1():
    import sqlite3
    connection = sqlite3.connect('bank.db')
    cursor = connection.cursor()

    os.system('cls')
    main_loop = True
    while main_loop:
        print()
        print()
        print('   Date :- ', dat)
        print()
        print('   1-Office Rent / 2-Staff Salary / 3-Office Electricity / 4-Office Stationery / 5-Office Transportation')
        acc = int(input('   Account Details :- '))
        description = input('   Description :- ')
        cr = int(input('   Credit :- '))
        de = int(input('   Debit :- '))
        ch = input('   Do you want to save ? :- (Y/N/ E- Exit)')
        ch1 = ch.upper()
        if ch1 == 'E':
            main_loop = False

        elif ch1 == 'Y':
            insert_record = """INSERT INTO alameercom (date, acc, des, credit, debit) VALUES (?, ?, ?, ?, ?);"""
            data = (dat, acc, description, cr, de)
            cursor.execute(insert_record, data)
            connection.commit()


choice_1()