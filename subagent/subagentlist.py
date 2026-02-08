

def choice_13():

    import sqlite3
    import os

    connection = sqlite3.connect('SubAgentAccount.db')
    cursor = connection.cursor()
    os.system('cls')
    print('')
    print('')
    print('   ---  LIST OF WORKERS DETAILS NUMBER  ---')
    print()
    print()
    select_all_record = """select * from SubAgent"""
    cursor.execute(select_all_record)
    records1 = cursor.fetchall()

    for row in records1:

            print(f"   {row[0]}       {row[1]}")

    print()
    press_key = input('      Press Enter Key to coutinue......')


