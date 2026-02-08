# to use current time
def choice_8():

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

    print()
    print()
    id = int(input('   Enter the Customer Code  :- '))
    select_all_record = """select * from SubAgent"""
    cursor.execute(select_all_record)
    records = cursor.fetchall()
    total = 0
    com = 0
    for row in records:
        if row[0] == id:
            subName = row[1]
            test = 1
            print("   Customer's Name  :- ", row[1])
            select_all_record = """select * from SubAgentDetails"""
            cursor.execute(select_all_record)
            records = cursor.fetchall()

            for y in records:
                if y[0] == id:
                    total = total + y[6]
                    com = com + y[7]
    grand_total = total - com
    print("   Total Outstanding Amount :- Rs. {:,.2f}".format(grand_total))
    print()
    key = input('   Press Any Key to .......')
    cursor.close()


