
def menu(spam):

    while True:

        choice = input('''
Please choose an option:

1. Sort the order of the values in the list (var.sort)
2. Reverse the order of the list (var.reverse)
3. Insert another value to the list (var.insert)
4. Remove all values from the list (var.clear)

 ''')


        if choice == '1':
            spam.sort()
        elif choice == '2':
            spam.reverse()
        #elif choice == '3':
        #    new_value = input('Enter the new value: ')
        #    spam.insert(new_value)
        #elif choice == '4':
        #    spam.clear()
        print('List values are currently: ')
#--------------------#
#Start of the program#
#--------------------#

spam = []
entry = input('Please enter the value to add: ')

if entry.isalpha() == False:
    entry = int(entry)

print('Variable type is: ', type(entry))
spam.append(entry)

print('List values are currently: ')
print(spam)

menu(spam)



