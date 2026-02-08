def choice_2():
    import sqlite3
    import os

    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n   ---  CHECK OUTSTANDING BALANCE BY PASSPORT NUMBER  ---\n')

    ppNumber = input('   Enter Passport Number :- ').upper()

    connection = sqlite3.connect('SubAgentAccount.db')
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM SubAgentDetails WHERE HousemaidPP = ?",
        (ppNumber,)
    )
    rows = cursor.fetchall()

    if not rows:
        print("\n   ❌ No records found.")
        input('\n   Press Enter...')
        cursor.close()
        connection.close()
        return   # ✅ valid because we are inside def

    total = 0
    comm = 0

    first = rows[0]
    print(f"\n   Customer's Code : {first[0]}   Customer's Name :- {first[1]}")
    print(f"   Passport No.:- {first[3]}    Housemaid Name :- {first[4]}")

    print("\n   Date        Description                 Amount")
    print("   ---------------------------------------------------")

    for row in rows:
        print(f"   {row[2]:<10} {row[5]:<25} Rs. {row[6]:>10,.2f}")
        total += row[6]
        comm += row[7]

    print("\n   Commission   :- Rs. {:,.2f}".format(comm))
    print("   Total Amount :- Rs. {:,.2f}".format(total))
    print("                       ----------")
    print("   Balance      :- Rs. {:,.2f}".format(comm - total))

    input('\n   Press Enter Key to Main Menu .....')

    cursor.close()
    connection.close()
