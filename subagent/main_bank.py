import sqlite3
import os
import datetime
import datereport
import alameer_comBank
import personnel_comBank
main_loop = True
while main_loop:

    os.system('cls')
    os.system('COLOR 0a')
    print()
    print()
    print('   ----- MAIN MENU -----')
    print()
    print('   1. Account Ledger ')
    print('   2. Personal Account Commercial Bank')
    print("   3. HNB Current Account")
    print('   0. Exit')
    print()
    choice_main = int(input('   Enter your choice :- '))
    if choice_main == 1:
        alameer_comBank.choice_1()
    elif choice_main == 0:
        main_loop = False
    elif choice_main == 2:
        personnel_comBank.choice_2()

os.system('color')
os.system('cls')