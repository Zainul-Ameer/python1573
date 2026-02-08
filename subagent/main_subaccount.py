import sqlite3
import os
import datetime
import addSubAgent
import OneHousemaidRecord
import SubAgentPayment
import addHmPassport
import dislplayHmRecord
import commission
import dep
import outstanding
import allsub
import subdetails
import reportHousemaid
import datereport
import subagentlist
import depHmDetails
main_loop = True
while main_loop:

   # os.system('cls')
   # os.system('COLOR 0a')
    print()
    print()
    print('   ----- MAIN MENU -----')
    print()
    print('   1. Add New Sub Agent')
    print('   2. Check Outstanding Balance by Passport Number')
    print("   3. Sub Agent Payment for Housemaid's Passport Number")
    print("   4. Add Housemaid's Record")
    print("   5. Display Workers Name List")
    print("   6. Commission ")
    print("   7. Departure ")
    print("   8. Sub Agent Outstanding ")
    print("   9. All Sub Agents Outstanding")
    print("  10. Sub Agent Outstanding details ")
    print("  11. Print Report Housemaid")
    print("  12. Report by Date")
    print("  13. Sub Agent List")
    print("  14. Departure Housemaid Account Details")
    print('   0. Exit')
    print()
    choice_main = int(input('   Enter your choice :- '))
    if choice_main == 1:
        addSubAgent.choice_1()
    elif choice_main == 0:
        main_loop = False
    elif choice_main == 2:
        OneHousemaidRecord.choice_2()
    elif choice_main == 3:
        SubAgentPayment.choice_3()
    elif choice_main == 4:
        addHmPassport.choice_4()
    elif choice_main == 5:
        dislplayHmRecord.choice_5()
    elif choice_main == 6:
        commission.choice_6()
    elif choice_main == 7:
        dep.choice_7()
    elif choice_main == 8:
        outstanding.choice_8()
    elif choice_main == 9:
        allsub.choice_9()
    elif choice_main == 10:
        subdetails.choice_10()
    elif choice_main == 11:
        reportHousemaid.choice_11()
    elif choice_main == 12:
        datereport.choice_12()
    elif choice_main == 13:
        subagentlist.choice_13()
    elif choice_main == 14:
        depHmDetails.choice_14()

#os.system('color')