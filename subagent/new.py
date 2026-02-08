

import datetime

# Import all the modules containing the functions for each menu option
import addSubAgent
import SubAgentPayment
import addHmPassport
import dislplayHmRecord
import commission
import dep
import OneHousemaidRecord
import outstanding
import allsub
import subdetails
import reportHousemaid
import datereport
import subagentlist
import depHmDetails
from utils import clear_screen

from colorama import init, Fore
init(autoreset=True)

# Define a dictionary to map menu options to functions
menu_options = {
    1: addSubAgent.choice_1,
    2: OneHousemaidRecord.choice_2,
    3: SubAgentPayment.choice_3,
    4: addHmPassport.choice_4,
    5: dislplayHmRecord.choice_5,
    6: commission.choice_6,
    7: dep.choice_7,
    8: outstanding.choice_8,
    9: allsub.choice_9,
    10: subdetails.choice_10,
    11: reportHousemaid.choice_11,
    12: datereport.choice_12,
    13: subagentlist.choice_13,
    14: depHmDetails.choice_14
}

main_loop = True
while main_loop:

    clear_screen()
    print()
    print()
    print(Fore.GREEN + '   ----- MAIN MENU -----')
    print()
    print(Fore.GREEN + '   1. Add New Sub Agent')
    print(Fore.GREEN + '   2. Check Outstanding Balance by Passport Number')
    print(Fore.GREEN + "   3. Sub Agent Payment for Housemaid's Passport Number")
    print(Fore.GREEN + "   4. Add Housemaid's Record")
    print(Fore.GREEN + "   5. Display Workers Name List")
    print(Fore.GREEN + "   6. Commission ")
    print(Fore.GREEN + "   7. Departure ")
    print(Fore.GREEN + "   8. Sub Agent Outstanding ")
    print(Fore.GREEN + "   9. All Sub Agents Outstanding")
    print(Fore.GREEN + "  10. Sub Agent Outstanding details ")
    print(Fore.GREEN + "  11. Print Report Housemaid")
    print(Fore.GREEN + "  12. Report by Date")
    print(Fore.GREEN + "  13. Sub Agent List")
    print(Fore.GREEN + "  14. Departure Housemaid Account Details")
    print(Fore.GREEN + '   0. Exit')
    print()
    choice_main = int(input(Fore.GREEN + '   Enter your choice :- '))
    if choice_main == 0:
        main_loop = False
    elif choice_main in menu_options:
        menu_options[choice_main]()
    else:
        print("Invalid choice. Please select a valid option.")

clear_screen()
