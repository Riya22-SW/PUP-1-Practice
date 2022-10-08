# 1.Triple all the numbers given in list
# x=map(lambda i:i*3,(1,2,3,4,5,6))
# print("\nTriple all numbers:")
# print(list(x))



# 2.Separate even odd number from given list
# tup_items=(1,3,7,8,4,5,2,15,6,22,12,89)
# x=map(lambda i:i%2==0,tup_items)
# print(list(x))



# 3.Print all string in lower case from given tuple
# def toLower(str):
#     return str.lower()
# x=map(toLower,("SOFTWARE","SEM","HELLO"))
# print(tuple(x))




# 4.Print square root of numbers given in list
# x=map(lambda i:i**0.5,(4,16,25,144,169,64,36,49,81,121))
# print((list(x)))




# 5.Eliminate duplicate letter from given string
# from collections import OrderedDict
#
#
# def remove_duplicate(str1):
#     return "".join(OrderedDict.fromkeys(str1))
#
#
# print(remove_duplicate("patel"))


# 6.Print table of any number
# def multiply(i):
#     return num*i
# num=int(input("Enter a number"))
# res=map(multiply,(1,2,3,4,5,6,7,8,9,10))
# print(list(res))




# 7.Add two list
# list1=["Banana","Mango","Watermelon"]
# list2=["Orange","Apple"]
# list1.extend(list2)
# print(list1)



# 8. Convert all float digits into integer using built in function from given list.
# num=[1.5,2.7,45.7,67.9,7.9]
# x=map(int,num)
# print(list(x))



# 9.Reverse given set

# list=[1,2,3,'a','b','c']
# list.reverse()
# print(list)


# 10.Add ‘@gmail.com’ to all the values of given dictionary and convert it to lower case
def toLower(str):
    return str.lower()
dict_item={"1":"RUTVI","2":"RIYA"}
a=map(lambda i:(i[0],i[1]+"@gmail.com"),dict_item.items())
print(dict(a))
new_dict = dict((k.lower(), v.lower()) for k, v in dict_item .items())
print(new_dict)

