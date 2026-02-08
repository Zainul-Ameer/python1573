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
    today_date = (x.strftime("%x"))
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
                select_all_record = """select * from SubAgentDetails"""
                cursor.execute(select_all_record)
                records = cursor.fetchall()

                for y in records:
                    if y[3] == housePassportNumber:
                        print("   Housemaid's Name  :- ", y[4])
                        houseName = y[4]
                        des = input("   Description  :- ")
                        dat = input('   Date  :- ')
                        amu = int(input("   Amount  :- "))
                        dep = 0
                        save_record = input('   Do you want to save this (Y/N)')
                        if save_record == 'Y':
                            insert_record = """INSERT INTO SubAgentDetails 
                            (SubId, SubName, DateCash, HousemaidPP, HousemaidName, Description, Credit, Depit) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
                            data = (id, subName, dat,  housePassportNumber, houseName, des, amu, dep)
                            cursor.execute(insert_record, data)
                            connection.commit()
                            choice = False
                            break
                        else:

                            choice = False
                            break


    cursor.close()
