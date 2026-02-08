# to use current time
def choice_9():

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
    select_all_record = """select * from SubAgent"""
    cursor.execute(select_all_record)
    records = cursor.fetchall()
    total = 0
    grand_total = 0
    for row in records:
        id = row[0]
        name = row[1]
        select_all_record = """select * from SubAgentDetails"""
        cursor.execute(select_all_record)
        records1 = cursor.fetchall()
        total = 0
        for row1 in records1:
            if row1[0] == id:
                total = total + row1[6]

        grand_total = grand_total + total
        if total > 0:
            print(f" {id}   {name}  --> Rs. {total} ")
    print()
    print("   Total Outstanding Amount :- Rs. {:,.2f}".format(grand_total))

    enter_key = input("   Press Enter Key.......")


    cursor.close()

