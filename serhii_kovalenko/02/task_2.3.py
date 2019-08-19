new_list = [1, 2, 3, 1, 3, 2, 1]

a = [i for i in new_list if new_list.count(i) % 2]

print(a[0])
