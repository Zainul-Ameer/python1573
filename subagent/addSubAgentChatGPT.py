import sqlite3

def choice_1():
    connection = sqlite3.connect('SubAgentAccount.db')
    cursor = connection.cursor()

    while True:
        id_num = int(input('Enter the id number (0 to exit): '))
        if id_num == 0:
            break

        cursor.execute("SELECT * FROM SubAgent WHERE id = ?", (id_num,))
        record = cursor.fetchone()
        if record:
            print('Customer I.D   :- ', record[0])
            print("Customer's name :- ", record[1])
            input('Already this code is exits...Press enter key!')
        else:
            subName = input('Sub Agent Name: ')
            if input('Do you want to Save this (Y/N)? ').lower() == 'y':
                cursor.execute("INSERT INTO SubAgent (id, Name) VALUES (?, ?)", (id_num, subName))
                connection.commit()

    cursor.close()
    connection.close()
