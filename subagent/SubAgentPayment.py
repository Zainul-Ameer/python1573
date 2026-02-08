# to use current time
def choice_3():

    import datetime

    # database
    import sqlite3


    import os   # to clear the screen when we run in dos prompt
    os.system('cls')

    # Sub Agent Table - List of Sub Agent Record
    connection = sqlite3.connect('SubAgentAccount.db')
    cursor = connection.cursor()

    # select all sub agents

    x = datetime.datetime.now()
    dat = (x.strftime("%x"))
    choice = True
    while choice:

        print()
        print()
        id = int(input('   Enter the Customer Code  :- '))
        if id == 0:
            break
        select_all_record = """select * from SubAgent"""
        cursor.execute(select_all_record)
        records = cursor.fetchall()
        for row in records:
            if row[0] == id:
                subName = row[1]
                test = 1
                print("   Customer's Name  :- ", row[1])
                housePassportNumber = input("   Housemaid's Passport Number  :- ")
                select_all_record = """select * from PassportHm"""
                cursor.execute(select_all_record)
                records = cursor.fetchall()
                pp = housePassportNumber.upper()

                for y in records:
                    if y[0] == pp:
                        print("   Housemaid's Name  :- ", y[1])
                        houseName = y[1]
                        des = input("   Description  :- ")
                        print('   Date  :- ', dat)
                        amu = int(input("   Amount  :- "))
                        py = int(input('   Payment by CASH-1 / ALAMEER COMBANK - 2 / PERSONNEL COMBANK-3 '))
                        dep = 0
                        save_record = input('   Do you want to save this (Y/N)? ')
                        a = save_record.upper()

                        if a == 'Y':
                            insert_record = """INSERT INTO SubAgentDetails 
                            (SubId, SubName, DateCash, HousemaidPP, HousemaidName, Description, Credit, Depit) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
                            data = (id, subName, dat,  pp, houseName, des, amu, dep)
                            cursor.execute(insert_record, data)
                            connection.commit()

                            if py == 2:
                                print('yes')
                                cer = 0
                                insert_record = """INSERT INTO alameercombank 
                                (date, des, credit, debit) VALUES (?, ?, ?, ?);"""
                                data = (dat, des, cer, amu)
                                cursor.execute(insert_record, data)
                                connection.commit()

                            choice = False
                            break
                        else:

                            choice = False
                            break


    cursor.close()