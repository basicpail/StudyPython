#try except 연습

# try:
#     radius = int(input("정수입력>"))

#     print("원의 반지름: ",radius)
#     print("원의 둘레: ",2*3.14,radius)
#     print("원의 넓이:",3.14,radius)

#     pass

# except:
#     print("입력오류")
#     pass

# list = ['11','22','ㅇㄹ','33','44','55','66']
# outputs = []

# for item in list:
#     try:
#         float(item)
#         outputs.append(item)
#         pass

#     except:
#         print("오류")
#         pass

# print(outputs)

try:
    radius = int(input("정수입력>"))

except:
    print("입력오류")
    pass
else:
    print("원의 반지름: ",radius)
    print("원의 둘레: ",2*3.14,radius)
    print("원의 넓이:",3.14,radius)
finally:
    print("프로그램종료")

