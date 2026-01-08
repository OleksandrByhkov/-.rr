import random

lst = [random.randint(0, 45) for el in range(random.randint(3, 10))]
print("Початковий список:", lst)
new_lst = [lst[0], lst[2], lst[-2]]
print("Новий список:", new_lst)
