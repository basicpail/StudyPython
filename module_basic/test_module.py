PI = 3.14159265

# print("모듈")
# print(__name__)

def number_input():
    output = input("숫자입력>")
    return float(output)

def get_circumference(radius):
    return 2*PI*radius

def get_circle_area(radius):
    return