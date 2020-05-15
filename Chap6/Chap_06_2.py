# def test():
#     print("test() 1")
#     try:
#         print("test() try")
#         return
#         print("test() after returning")
#     except:
#         print("test exception")
#     else:
#         print("test() else")
#     finally:
#         print("test() finally")

#     print("test() end")

# test()


# try:
#     radius = int(input("정수입력>"))
#     print("원의 반지름: ",radius)
#     print("원의 둘레: ",2*3.14,radius)
#     print("원의 넓이:",3.14,radius)

# except Exception as ex:
#     print(type(ex))
#     print(ex)
#     pass

# finally:
#     print("프로그램종료")

# list = [52,274,32,72,100]

# try:
#     number_input = int(input("정수 입력>"))

#     print("{}번째 요소:{}".format(number_input,list[number_input]))

# except ValueError as ex:
#     print(type(ex))
#     print(ex)
#     print("정수를 입력하세요.")

# except Exception as exception:

#     print("type(exception:",type(exception))
#     print("exception:", exception)



try:
    number = int(input("정수 입력>"))

    if number > 0:
        raise NotImplementedError("0보다 큼: 구현안됨")
    else:
        raise NotImplementedError("0보다 작음: 구현안됨")
except NotImplementedError as ex:
    print(ex)
    pass
except ValueError as ex:
    print("정수를 넣으세요.")
except Exception as ex:
    print(type(ex))
    print(ex)
finally:
    print("무조건 실행")
    pass