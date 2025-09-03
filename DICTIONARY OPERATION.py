print("\t\t\t DICTIONARY OPERATION")
my_dict={"name":"dhanu","age":19,"city":"trichy"}
my_diprintct=dict(name="dhanu",age=19,city="trichy")
print("\n Initially,my_dict:",my_dict)
print("\n my_dict[name]:" ,my_dict["name"])
print("\n update age as 31 in my_dict:")
my_dict["age"]:31
print("Now,my_dict:",my_dict)
print("Delete dict in my_dict:")
del my_dict["city"]
print("\n Now,my_dict:",my_dict)
print("\n Name in my_dict")
print("Name" in my_dict)
print("\n Address in my_dict:")
print("Address" in my_dict)
print("\n key in my_dict")
for Key in my_dict:
  print(Key)
print("\n values in my_dict")
for values in my_dict.values():
    print(values)
print("\n Key value pair in my_dict")
for Key,values in my_dict.items():
    print(Key,values)
print("\n Now no of values in my_dict")
print(len(my_dict))
