immutable_var =  1, 2, "Hello", True
print(immutable_var)
# immutable_var [0] = 5  # кортеж является неизменяемой величиной, изменение элементов кортежа не возможно

mutable_list = ["Bye", 5, 98, False]
mutable_list[1] = 10
print(mutable_list)
