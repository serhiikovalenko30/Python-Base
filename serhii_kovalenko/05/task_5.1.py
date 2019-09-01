# One common problem when prompting for numerical input occurs when people provide text instead of numbers.
# When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers.
# Add them together and print the result. Catch the ValueError if either input value is not a number, and print a
# friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.

# creating a variable with a file name
file = 'results.txt'

while True:
    try:
        a = input('Enter a: ')
        if a == 'q':
            break
        b = input('Enter b: ')
        if b == 'q':
            break
        result = int(a) + int(b)
    except ValueError:
        print('You entered text instead of a number')
    else:
        with open(file, 'a') as f:
            f.write(f'{str(result)}\n')
