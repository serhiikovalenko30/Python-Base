any_text = input('Enter any text for reverse: ')

reverse_string = ''
count = 0

for i in any_text:

    count += 1
    a = len(any_text) - count
    reverse_string += any_text[a]

print(reverse_string)
