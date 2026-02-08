# to use current time
def choice_6():

    import datetime
    from utils import clear_screen

    # database
    import sqlite3

    clear_screen()

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
        records_SubAgent = cursor.fetchall()
        for row in records_SubAgent:
            if row[0] == id:
                subName = row[1]
                test = 1
                print("   Customer's Name  :- ", row[1])
                housePassportNumber = input("   Housemaid's Passport Number  :- ")
                select_all_record = """select * from PassportHm"""
                cursor.execute(select_all_record)
                records_PassportHm = cursor.fetchall()

                for y in records_PassportHm:
                    if y[0] == housePassportNumber:
                        print("   Housemaid's Name  :- ", y[1])
                        houseName = y[1]
                        des = "Commission"
                        print("   Description  :- ", des)
                        dat = input('   Date  :- ')
                        print("   Amount  :- ", y[2])
                        amu = 0
                        dep = y[2]
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


