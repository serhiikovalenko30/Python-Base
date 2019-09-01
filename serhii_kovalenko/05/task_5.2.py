# Edit your previous task: put the results into a file. Then create a new python script and import your previous
# program to the new script. Write a program that reads the file and prints it three times. Print the contents once by
# reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then
# working with them outside the 'with' block.


# import previous program. Does not work with point, commented on this
import task

# work with file and print the contents once by reading in the entire file
print('\nOnce by reading in the entire file:')
with open(task.file, 'r') as f:
    file_info = f.read()
    print(file_info)

# work with file and print by looping over the file object
print('\nBy looping over the file object:')
with open(task.file, 'r') as f:
    for i in f:
        print(i.rstrip())

# work with file and print by storing the lines in a list and then working with them outside the 'with' block
print('\nBy storing the lines in a list:')
with open(task.file, 'r') as f:
    file_info = f.readlines()

for i in file_info:
    print(i.rstrip())


