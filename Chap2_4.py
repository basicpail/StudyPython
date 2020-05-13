# format_a = "{}".format(10)
# format_b = "{} {}".format(10,20)

# format_c = "파이썬 열공하여 첫 연봉 {} 만 원 만들기".format(50000)

# output_a = "{:d}".format(30)

# # print(format_a)
# # print(format_b)
# # print(type(format_b))
# # print(format_c)

# print(output_a)
# output_a = 40
# print(output_a)

# output_b = "{:g}".format(3.3500)
# print(output_b)

# input_s = "Hello Python Programming!!"
# input_t = """
#             안녕하세요          
# 테스트 입니다.
# """

# print(input_s.upper())
# print(input_s.lower())
# print(input_t.strip())

check_str = "TrainA10"
print(check_str.isalnum())
print(check_str.find("A"))

print("하세" in "안녕하세요")
a = "10 20 30 40 50 60".split(" ")
b = "10|20|30|40|50|60".split("|")
print(a)
print(b)