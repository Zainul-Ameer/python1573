def choice_10():
    import sqlite3

    from utils import clear_screen
    connection = sqlite3.connect('SubAgentAccount.db')
    cursor = connection.cursor()

    clear_screen()

    # --- Get Sub Agent ---
    cursor.execute("SELECT * FROM SubAgent")
    records2 = cursor.fetchall()

    cursor.execute("SELECT * FROM SubAgentDetails")
    records1 = cursor.fetchall()

    code = int(input('   Enter the Sub Agent Code Number :- '))

    sub_agent_name = "UNKNOWN"
    for row2 in records2:
        if row2[0] == code:
            sub_agent_name = row2[1]
            break

    clear_screen()

    print('\n   ---  ACCOUNT DETAILS  ---\n')
    print(f'   Code :- {code}    Name :- {sub_agent_name}\n')

    # ---- Table Header ----
    print("   {0:<12} {1:<15} {2:<20} {3:<25} {4:>12}".format(
        "Date", "Passport", "Housemaid", "Description", "Amount"
    ))
    print("   " + "-" * 90)

    total = 0
    com = 0

    for row in records1:
        if row[0] == code:
            print("   {0:<12} {1:<15} {2:<20} {3:<25} Rs. {4:>9,.2f}".format(
                row[2], row[3], row[4], row[5], row[6]
            ))
            total += row[6]
            com += row[7]

    print("\n   " + "-" * 90)
    print("   {0:<74} Rs. {1:>9,.2f}".format("Total Outstanding Amount", com - total))

    input('\n      Press Enter Key to continue......')

    cursor.close()
    connection.close()
