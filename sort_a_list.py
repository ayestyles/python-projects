


def reverse_order(self):
    spam.reverse()
#   print(spam)


def default_sort(self):
    spam.sort()
#   print(spam)

def want_to_sort(self):
    choice = input('''

Type 1 to use the default Sort method
Type 2 to use the reverse Sort method''')

    if choice == '1':
        default_sort(spam)
    elif choice == '2':
        reverse_order(spam)

#def analyze_list():


entry_1 = input('Please enter the first NUMERIC char: ')
entry_2 = input('Please enter the second NUMERIC char: ')
entry_3 = input('Please enter the third NUMERIC char: ')

if entry_1.isalpha() == False:
    entry_1 = int(entry_1)

if entry_2.isalpha() == False:
    entry_2 = int(entry_2)

if entry_3.isalpha() == False:
    entry_3 = int(entry_3)

print(type(entry_1))
print(type(entry_2))
print(type(entry_3))




spam = [entry_1, entry_2, entry_3]

#spam[0] = int(spam[0])
#spam[1] = int(spam[1])
#spam[2] = int(spam[2])


print('Printed values are: ')
print(spam)


to_sort = input('Would you like to sort your new list? ')
if to_sort == 'y':
    want_to_sort(spam)
    print('The modified order is ')
    print(spam)

if to_sort == 'n':
    print('Well that is boring!')