

def choice_5():

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
    select_all_record = """select * from PassportHm"""
    cursor.execute(select_all_record)
    records1 = cursor.fetchall()
    total = 0
    i = 0
    len_name = 0
    for row in records1:
        if len(row[1]) > len_name:
            len_name = len(row[1])
    name_str = ' '
    for row in records1:
        i += 1
        if i >= 10:
            name = row[1]
            no_of_space = len_name - len(name)
            if len(name) < len_name:
                name = name + (name_str * no_of_space)

            print(f" {i}.  {row[0]}   {name}      {row[4]}")
        else:
            name = row[1]
            no_of_space = len_name - len(name)
            if len(name) < len_name:
                name = name + (name_str * no_of_space)

            print(f"  {i}.  {row[0]}   {name}      {row[4]}")


    print()
    press_key = input('      Press Enter Key to coutinue......')