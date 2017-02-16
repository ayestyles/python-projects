#Ask for input from the user and then sort the list based on what they put in alpha-numeric order


def reverse_order(reversed_value):
    spam.reverse()

def default_sort(default_sorted_value):
    spam.sort()

def want_to_sort(spam)
    while True:
        choice = input('''

    Type 1 to use the default Sort method
    Type 2 to use the reverse Sort method''')

        if choice == '1':
            default_sort(spam)
        elif choice == '2':
            reverse_order(spam)
        elif choice == '3':
            break
        else:
            continue



while True:

    entry_1 = input('Please enter the first alpha-numeric char: ')
    entry_2 = input('Please enter the second alpha-numeric char: ')
    entry_3 = input('Please enter the third alpha-numeric char: ')

    spam = [entry_1, entry_2, entry_3]
    print('You entered: ')
    print(spam)

    to_sort = input('\n Would you like to sort your new list? ')
    if to_sort == 'y':
        continue
    if to_sort == 'n':
        break




    print('The modified order is ')
    print(spam)
