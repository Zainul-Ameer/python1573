"""
From this you can check given passport number of housemaid's expenses under sub - agent name
"""


def choice_11():
    from utils import clear_screen
    import sqlite3
    import os

    os.remove("disply.txt")
    connection = sqlite3.connect('SubAgentAccount.db')
    cursor = connection.cursor()
    os.system('cls')
    print('')
    print('')
    print('   ---  CHECK OUTSTANDING BALANCE BY PASSPORT NUMBER  ---')
    print()
    ppNumber = input('   Enter Passport Number :- ')
    os.system('cls')
    print()
    print()
    select_all_record = """select * from SubAgentDetails"""
    cursor.execute(select_all_record)
    records1 = cursor.fetchall()
    total = 0
    comm = 0
    for row in records1:
        if row[3] == ppNumber.upper():
            print(f"   Customer's Code : {row[0]}   Customer's Name :- {row[1]}")
            print(f'   Passport No.:- {row[3]}    Housemaid Name :- {row[4]}')

            with open('disply.txt', 'a') as f:
                f.write(f"   Customer's Code : {row[0]}   Customer's Name :- {row[1]} \n")
                f.write(f'   Passport No.:- {row[3]}    Passenger Name :- {row[4]} \n')
                f.write('********************************************************* \n')
            ppNumber = row[3]
            break

    for row in records1:
        if row[3] == ppNumber:
            if row[6] != 0:

                with open('disply.txt', 'a') as f:

                    f.write(f"   Date :- {row[2]} \n")
                    f.write(f"   Description :- {row[5]} \n")
                    f.write("   Amount :- Rs. {:,.2f} \n".format(row[6]))
                    f.write('------------------------------- \n')

            total = total + row[6]
            comm = comm + row[7]

    with open('disply.txt', 'a') as f:
        f.write("   Total Amount :- Rs. {:,.2f}".format(total))
    bal = comm - total
    enter_key = input('   Report Created and Press Enter Key to Main Menu .....')
    f.close()
    cursor.close()

