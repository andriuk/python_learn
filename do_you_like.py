from multiprocessing.sharedctypes import Value

value = input('Would you like continue')

if value == 'y' or value == 'yes':
   print('Continue ...')
   print('Complete!')
elif value == 'n' or value == 'no' :
   print('Exiting')
else:
   print('Please try again and respond with yes or no')
