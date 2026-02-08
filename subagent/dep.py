# to use current time
def choice_7():
    import datetime
    # database
    import sqlite3
    import os   # to clear the screen when we run in dos prompt

    # Sub Agent Table - List of Sub Agent Record
    connection = sqlite3.connect('SubAgentAccount.db')
    cursor = connection.cursor()

    # select all sub agents

    x = datetime.datetime.now()
    today_date = (x.strftime("%x"))

    print()
    print()
    housePassportNumber = input("   Housemaid's Passport Number  :- ")
    select_all_record = """select * from SubAgentDetails"""
    cursor.execute(select_all_record)
    records = cursor.fetchall()

    for y in records:
        if y[3] == housePassportNumber:
            save_record = input('   Do you want to save this (Y/N)')
            if save_record == 'Y':
                break

    for y in records:
        if y[3] == housePassportNumber:
            id = y[0]
            subName = y[1]
            dat = y[2]
            ppNumber = y[3]
            maidName = y[4]
            des = y[5]
            amu = y[6]
            dep = y[7]
            insert_record = """INSERT INTO depHousemaid
            (Id, SubName, Date, ppno, HmName, Des, cre, deb) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
            data = (id, subName, dat,  ppNumber, maidName, des, amu, dep)
            cursor.execute(insert_record, data)
            connection.commit()

    cursor.close()
