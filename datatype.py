#print("hello python")
#useVar=input("Enter String: ");y=50
#print(f"y={y}")
#print("y=",y)
#floatX=float(input("enter float value : "))
#print(f"float values is {floatX}")
#a=b=c=80
#print(f"a={a}, b={b}, c={c}")
#ax,bx,cx=50,20,3.5
#print(f"ax={ax}, bx={bx}, cx={cx}")

#arthmetic operation
#a=b=20
#print(f"Addition: {a+b}")

#datatype
int_var=10

float_var=20.5

string_var="hello"

bool_var=True

#list
list_var=[12,23.3,94,20]
print(f"list = {list_var}");print(f"list index1={list_var[1]}")
print(f"list = {list_var[:]}");print(f"list ind1to3 = {list_var[1:4]}")
print(f"list last index = {list_var[-1]}")
print(f"list ind4to1 = {list_var[-1:-5:-1]}")
list_var[2:]=10,20,30
print(list_var)
list_var.append(7)
print(f"after append={list_var}")
list_var.extend([99,88.45,99])
print(f"extend list= {list_var}")
list_var.insert(2,75)
print(f"after inserting= {list_var}")
list_var.pop(2)
print(f"after pop= {list_var}")
list_var.remove(99)
print(f"after pop= {list_var}")
list_var.sort()
print(f"after sort= {list_var}")
list_var.reverse()
print(f"after reverse= {list_var}")

#tuple
tuple_var=(11,77,22,44)
print(tuple_var+(12,55))
print(f"tuple = {tuple_var}");print(f"tuple index1={tuple_var[1]}")
print(f"tuple = {tuple_var[:]}");print(f"tuple ind1to3 = {tuple_var[1:4]}")
print(f"tuple last index = {tuple_var[-1]}")
print(f"tuple ind4to1 = {tuple_var[-1:-5:-1]}")

#set
set_var={54,46,67,88,22,44}
print(f"type of set_var = {type(set_var)}")
set_var.add(5)
print(f"after add= {set_var}")
set_var.discard(88)
print(f"after discard= {set_var}")
union_set=set_var.union({44,22,64})
print(f"union set= {union_set}")
set_difference=set_var.difference(union_set)
print(f"set difference= {set_difference}")

#dict
dict_var={1:'A','S':2}
print(f"dictionary = {dict_var}")
dict_var['c']=3
print(f"added new value in dictionary = {dict_var}")
dict_var[1]=44
print(f"updated dictionary key 1 = {dict_var}")
dict_var.pop('c')
print(f"remove dictionary key C = {dict_var}")
keys=dict_var.keys()
print(f"key of dictionary = {keys}")
values=dict_var.values()
print(f"value of dictionary = {values}")
items=dict_var.items()
print(f"items of dictionary = {items}")


