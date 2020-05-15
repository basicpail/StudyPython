# 마지막 테스트 파이썬
import json

dic_mcu = []

# print(dic_mcu)
# with open("./data/mcu_movies.json", "w", encoding="UTF-8") as mcu_list:
#   json.dump(dic_mcu, mcu_list, ensure_ascii=False)

with open("./final/mcu_movies.json", "r", encoding="UTF-8") as mcu_list:
  dic_mcu = json.load(mcu_list)


# 문제 1번
# 페이즈가 1인 마블 시네마틱 유니버스 영화면 뽑기

# print(dic_mcu)

for item in dic_mcu:
  if item["시리즈"] == '페이즈2':
    print("{} ({})".format(item["영화명"],item["개봉일"]))
  
# 문제 2번
# 박스오피스가 450000000 이상인 영화들의 감독이름 리스트와 전체 합계금액, 평균 박스오피스 구하기
Dirlist = []
cnt = 0
sum = 0
for item in dic_mcu:
  if item["박스오피스"] >= 450000000:
    if not item["감독"] in Dirlist :
      Dirlist.append(item["감독"])
    cnt += 1
    sum += item["박스오피스"]

avg = sum//cnt

print("감독 리스트:\n",set(Dirlist))
print("총 박스오피스 합계 $ {:,}".format(sum))
print("평균 박스오피스 $ {:,}".format(avg))