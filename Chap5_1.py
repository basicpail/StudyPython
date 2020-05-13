def print_():
    for i in range(5):
        print("Hello World")



# def print_n_times(value, n):
#     for i in range(n):
#         print(value, end= " ")



#   def print_n_times(n, *values):
#      for i in range(n):
#          for value in values:
#              print(value, end = " ")

def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value, end =" ")
        print()

# print_()
# print_n_times("Hello", 4)
# print_n_times(4, "안녕하세요", "즐거운","프로그래밍입니다")

# print_n_times("Hello","안녕하세요",n=3)

# def func(a,b=10,c=20):
#     print(a+b+c)


# func(c=100, a=50, b= 50)

# def return_test():
#     print("Value A")
#     return 100
#     print("Value B")

# value = return_test()
# print("Value 는 {}".format(value))

# if(value == None):
#     print("value값이 없습니다")
# else:
#     print("value는 {}".format(value))

def multi_all(start, end):
    output = 1

    for i in range(start, end+1):
        output *= i
    
    return output

print("0 to 100", multi_all(1,100))