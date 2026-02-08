import sqlite3
connection = sqlite3.connect('SubAgentAccount.db')
cursor = connection.cursor()


customer_id = int(input('  Enter Code Number :- '))
customer_name = input('   Sub Agent Name :- ')

insert_record = """INSERT INTO SubAgent 
(id, Name) VALUES (?, ?);"""
data = (customer_id, customer_name)
cursor.execute(insert_record,data)
connection.commit()
cursor.close()