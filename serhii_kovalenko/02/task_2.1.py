any_text = input('Enter any text for verification: ')

count_o = [sym for sym in any_text if sym == 'o' or sym == 'O']
count_x = [sym for sym in any_text if sym == 'x' or sym == 'X']

if len(count_o) == len(count_x):

    print('True')

else:

    print('False')
