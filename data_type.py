# THere are two major category of data type in python
# 1. Mutable ---->list, dict,set, Array, Bytearray
# 2. Imutable----->number, string, boolean,tuple,frozen set, bytes

# NUMBER DATA TYPE
# 1. int
# 2. float
# 3. complex

a = 10; b=-10 # int type
f = 14.2; f2= 12/2 # float type

cpm = 3j; cpm2= 2+5j # compelx type where is denote imaginary number and 2 denote real number, something its come 2i+5j

# STRING DATA TYPE
# str
name = "akash Raja" # str type
# print(name.index("R"))

# BOOLEAN DATA TYPE
isTrue = True; isFalse = False # bool type





#LIST/ ARRAY
# LIST is a REPLCEMENT OF AN ARRAY

fruit = ["orange","Apple","papaya","cherry","Banana"]

empty = [] # empty list

# formating of list destructure od an array

a,b,c =[1,2,3]
# print(a) #1
# print(b) #2
# print(c) #3
list =  [5,4,100,99,0,-10,4]
# print(len(fruit)) # is method to find length of list

# fruit.append("chilli")
# list.sort()
# list.reverse()
# fruit.pop(2)
# list.remove(99)
# new_list =list.copy()
# list.insert(2,700)
# list[5] = 780 # update value
# count=0
# for key in list:
   
#     print(count, key)
#     count+=1

# if 100 in list:
#         print("we have this number")

# print(list)

# empty.append("tery bear")
# print(empty)







#--------Dictionary----------- replacement of object 

dict ={"name":"akash","age":24,"location":"Noida","tpl":[1,5,6]}

list =[4,5,8,7]

# dict.get("name")
# dict["age"]
# dict.pop("age")
# new_dict =dict.copy()
# dict.value() # return all values
# dict.keys() # return all keys
# for key,value in dict.items():
#     print(key,value)

# for key in dict:
#     print(key)

# if "name" in dict:
#     print("yes")
# else:
#     print("NO fount")


# del dict["name"]
# del dict
# dict.clear()
# print(dict)




# tuple --immutable
tpl =("orange","banana","apple","cherry","apple") 

# for key in tpl:
#     print(key)
# tpl.index("orange")
# res = tpl.count("apple")
# print(res)



# --------------- set data type---------


fruit= {"orange","banana","apple","cherry","grauva","ram"}
s=set()
s.add("orange")
s.add("banana")
s.add("apple")
s.add("cherry")

# fruit.pop()
# fruit.remove("apple")
# fruit.clear()
# res = s.issubset(fruit)

# for i in fruit:
#     if "mm" in fruit:
#        print("yes")
#        break
     
       
 
# print(res)


 