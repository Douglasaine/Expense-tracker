#create the categories and set them at 0
CATEGORIES = {
    'Food': 0,
    'Transportation': 0,
    'Services': 0,
    'Pets': 0,s
    'Entertainment': 0,
    'Others': 0
}

MENU_PROMPT = ''' Welcome! 
        If you want to see your expenses type "S"
        If you want to add a new expense type "A" 
        If you want to quit the app type "Q" '''

CATEGORIES_PROMPT = '''Please, select a category to add your expense:
            TYPE 'F' FOR FOOD 
            TYPE 'T' FOR TRANSPORTATION
            TYPE 'S' FOR SERVICES
            TYPE 'E' FOR ENTERTAINMENT 
            TYPE 'O' FOR OTHERS
            
            
            '''


def add_expenses(): #select the categorie and add expenses
    select_categorie = input(CATEGORIES_PROMPT).upper()

    expense = int(input('enter the amount'))

    if select_categorie == 'F':
        CATEGORIES['Food'] += expense
    if select_categorie == 'T':
        CATEGORIES['Transportation'] += expense
    if select_categorie == 'S':
        CATEGORIES['Services'] += expense
    if select_categorie == 'E':
        CATEGORIES['Entertainment'] += expense
    if select_categorie == 'O':
        CATEGORIES['Others'] += expense


def see_tracker():
    print(f'''
          FOOD: {CATEGORIES['Food']}
          TRANSPORTATION: {CATEGORIES['Transportation']}
          SERVICES: {CATEGORIES['Services']}
          PETS: {CATEGORIES['Pets']}
          ENTERTAINMENT: {CATEGORIES['Entertainment']}
          OTHERS: {CATEGORIES['Others']}''')

def main_menu():
    while True:
        user_option = input(MENU_PROMPT).upper()
        if user_option == 'S':
                see_tracker()
        if user_option == 'A':
                add_expenses()
        if user_option == 'Q':
                break

main_menu()













