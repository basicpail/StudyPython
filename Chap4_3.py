# for i in range(0,5,2):
#     print(i, " = 반복변수")



# array = [11,22,33,44,55,66]
# for i in array:
#     print(i)

# print(" ")


# for i in range(5,0,-1,-1):
#     print("{}".format(i))

# i=0
# while i<10:
#     i += 1
#     print(i)

# i=0
# while i<10:
#     print("{}번째 반복".format(i))
#     i += 1

#     input_text = input("> 종료합니까?(y)")
#     if input_text in ["y","Y"]:
#         print("반복n 종료")
#         break

# number = [5,15,6,60,7,25]

# for num in number:
#     if num<10:
#         continue

#     print(num)

example_list = ["itemA","itemB","itemC","itemD"]

print(example_list)
print()

print(enumerate(example_list))
print()

print(list(enumerate(example_list)))

for i,value in enumerate(example_list):
    print("{}번째 요소는 {}".format(i, value))

print()

example_dict = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C",
    "키D" : "값D",
}

print(example_dict.items())

for key,element in example_dict.items():
    print("dictionary[{}] = {}".format(key, element))

print()