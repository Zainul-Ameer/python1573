import os
from importlib import import_module

menu_options = {
    1: 'addSubAgent.choice_1',
    2: 'OneHousemaidRecord.choice_2',
    3: 'SubAgentPayment.choice_3',
    4: 'addHmPassport.choice_4',
    5: 'dislplayHmRecord.choice_5',
    6: 'commission.choice_6',
    7: 'dep.choice_7',
    8: 'outstanding.choice_8',
    9: 'allsub.choice_9',
    10: 'subdetails.choice_10',
    11: 'reportHousemaid.choice_11',
    12: 'datereport.choice_12',
    13: 'subagentlist.choice_13',
    14: 'depHmDetails.choice_14'
}

main_loop = True
while main_loop:
    print('\n\n   ----- MAIN MENU -----')
    for i in range(1, 15):
        print(f'   {i}. {import_module(menu_options[i]).__doc__}')
    print('   0. Exit')

    choice_main = int(input('   Enter your choice :- '))
    if choice_main == 0:
        main_loop = False
    elif choice_main in menu_options:
        import_module(menu_options[choice_main])()
    else:
        print("Invalid choice. Please select a valid option.")
