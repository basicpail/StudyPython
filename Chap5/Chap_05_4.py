import random

hanguls = list("민경수진욱상은근윤진태재승하")

with open("./data/result.txt","w") as f:
    # f.write("{},{},{}\n".format("이름","몸무게","키"))
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(45,90)
        height = random.randrange(150,190)

        f.write("{},{},{}\n".format(name,weight,height))

print("파일 생성이 완료되었습니다.")