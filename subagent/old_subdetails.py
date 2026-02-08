def choice_10():
    import sqlite3
    import os

    connection = sqlite3.connect('SubAgentAccount.db')
    cursor = connection.cursor()
    #os.system('cls')
    select_all_record = """select * from SubAgent"""
    cursor.execute(select_all_record)
    records2 = cursor.fetchall()
    print()
    print()
    select_all_record = """select * from SubAgentDetails"""
    cursor.execute(select_all_record)
    records1 = cursor.fetchall()
    code = int(input('   Enter the Sub Agent Code Number :- '))
    for row2 in records2:
        if row2[0] == code:
            sub_agent_name = row2[1]

    #os.system('cls')
    print('')
    print('')
    print('   ---  ACCOUNT DETAILS  ---')
    print()
    print(f'   Code :- {code}    Name :- {sub_agent_name}')
    print()

    total = 0
    com = 0
    lenth = 0
    lenth1 = 0
    hm_name_len_new = 0
    for row in records1:
        if row[0] == code:
            des = row[5]
            hm_name = row[4]
            hm_name_len = len(hm_name)
            lenth = len(des)
            if lenth > lenth1:
                lenth1 = lenth
            if hm_name_len > hm_name_len_new:
                hm_name_len_new = hm_name_len
    amount_str = ''
    for row in records1:
        if row[0] == code:
            des = row[5]
            hm_name = row[4]
            a5 = len(row[5])
            hm_name_len = len(hm_name)
            a = ' '
            amount_len = 12
            if a5 < lenth1:
                c5 = lenth1 - a5
                a1 = a * c5
                des = des + a1
            if hm_name_len < hm_name_len_new:
                add_space_number = hm_name_len_new - hm_name_len
                add_space = a * add_space_number
                hm_name = hm_name + add_space
                amount = "{:,.2f}".format(row[6])
               # amount_str = str(amount)
              #  amount_str_len = len(amount_str)
                #if amount_str_len < 12:
                #    ab = 12 - amount_str_len
                  #  a = a * ab
                  #  amount_str = a + amount_str

            print(f'    {row[2]}    {row[3]}    {hm_name}      {des}     {amount} ')
            total = total + row[6]
            com = com + row[7]

    grand_total = com - total
    print()
    print("    Total Outstanding Amount :- Rs. {:,.2f}".format(grand_total))
    print()
    press_key = input('      Press Enter Key to coutinue......')



