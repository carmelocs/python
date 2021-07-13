ans = input('Would you like to continue?')

if ans=='yes' or ans=='y':
    print(f'Continuing ...\nComplete!')
elif ans=='no' or ans=='n':
    print(f'Exiting')
else:
    print(f'Please try again and respond with yes or no.')