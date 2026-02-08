"""
From this you can check given passport number of housemaid's expenses under sub - agent name
"""


def choice_14():

    import sqlite3
    import os
    connection = sqlite3.connect('SubAgentAccount.db')
    cursor = connection.cursor()
   # os.system('cls')
    print('')
    print('')
    print('   ---  CHECK OUTSTANDING BALANCE BY PASSPORT NUMBER  ---')
    print()
    ppNumber = input('   Enter Passport Number :- ')
    #os.system('cls')
    print()
    print()
    select_all_record = """select * from depHousemaid"""
    cursor.execute(select_all_record)
    records1 = cursor.fetchall()
    total = 0
    comm = 0
    a = ' '
    amount_len = 12
    for row in records1:
        if row[3] == ppNumber.upper():
            print(f"   Customer's Code : {row[0]}   Customer's Name :- {row[1]}")
            print(f'   Passport No.:- {row[3]}    Housemaid Name :- {row[4]}')
            ppNumber = row[3]
            break
            a = ' '

    for row in records1:
        if row[3] == ppNumber:

            amount = "{:,.2f}".format(row[6])
            amount_str = str(amount)
            amount_str_len = len(amount_str)
            if amount_str_len < 12:
                ab = 12 - amount_str_len
                a = a * ab
                amount_str = a + amount_str

            print('')
            amount = "{:,.2f}".format(row[6])
            print(f"    {row[2]}     {row[5]}    {amount}")

            total = total + row[6]
            comm = comm + row[7]

    print()

    print("   Commission   :- Rs. {:,.2f}".format(comm))
    print("   Total Amount :- Rs. {:,.2f}".format(total))
    print("                       ----------")
    bal = comm - total
    print("   Balance      :- Rs. {:,.2f}".format(bal))
    print()
    enter_key = input('   Press Enter Key to Main Menu .....')

    cursor.close()


