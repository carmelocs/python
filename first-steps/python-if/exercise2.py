print('data types of a string, integer, and Boolean value')
print(type('Hello World'))
print(type(7))

print(type(True))
print(type(False))

print(type('True'))
print(type('False'))
print(f'\nbuilt-in bool() function to convert various string values to Boolean values')
print(bool('True'))
print(bool('False'))
print(bool(''))
print(bool(' '))
print(bool('Hello world!'))

print(f'\nbuilt-in bool() function to convert various integer values to Boolean values')
print(bool(7))
print(bool(1))
print(bool(0))
print(bool(-1))

print(f'\nBoolean expression')
print(1+1==3)
print(1+1==2)

print(f'\nComparison operators')
print(3 == 4)
print(3 != 4)

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)

print(f'\nLogical operators')
first_number = 5
second_number = 0
true_value = True
false_value = False

if first_number > 1 and first_number < 10:
    print('The value is between 1 and 10.')

if first_number > 1 or second_number > 1:
    print('At least one value is greater than 1')

print(not true_value)
print(not false_value)

if not first_number > 1 and second_number < 10:
    print('Both values pass the test')
else:
    print('Both values do NOT pass the test')