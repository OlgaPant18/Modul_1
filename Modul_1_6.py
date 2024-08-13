my_dict = {"Anna": 1986, "Boris": 1956, "Sveta": 1979, "Misha": 2004}
print(my_dict)
print(my_dict["Sveta"])
print(my_dict.get("Sasha"))
my_dict.update ({"Lena": 1959, "Katya": 2015})
net_ = my_dict.pop ("Boris")
print(net_)
print(my_dict)

my_set = {5, "Hello", 3, 4, "Bye", "Hello", 5, 4}
print(my_set)
my_set.update({6, 9})
my_set.remove(5)
print(my_set)
