# def create_student(name, korean, math, english, science):
#     return{
#         "name":name,
#         "korean":korean,
#         "math":math,
#         "english":english,
#         "science":science
#     }

# students = [
#     create_student("김상근" , 87, 23,99,100 ),
#     create_student("박상근" , 86, 99,39,80 ),
#     create_student("이상근" , 85, 88,79,70 ),
#     create_student("최상근" , 82, 57,89,90 ),
#     create_student("신상근" , 85, 74,29,80 ),
#     create_student("정상근" , 81, 76,99,30 )
# ]

# print("이름","총점","평균",sep="\t")
# for student in students:
#     score_sum = student["korean"]+student["math"]+\
#         student["english"] + student["science"]
#     score_average = score_sum/4

#     print(student["name"], score_sum, score_average, sep="\t")

class Student:
    def __init__(self,name,korean,math,english,science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math+\
            self.english + self.science

    def get_average(self):
        return self.get_sum()/4

    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())


students = [
    Student("김상근" , 87, 23,99,100 ),
    Student("박상근" , 86, 99,39,80 ),
    Student("이상근" , 85, 88,79,70 ),
    Student("최상근" , 82, 57,89,90 ),
    Student("신상근" , 85, 74,29,80 ),
    Student("정상근" , 81, 76,99,30 )
]

print("이름","총점","평균",sep="\t")
for student in students:
    print(student.to_string())
