from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

soup = BeautifulSoup(target, "html.parser")

for locate in soup.select('location'):
    print(F"도시: { locate.select_one('city').string }")
    print(F"날씨: { locate.select_one('wf').string }")
    print(F"최저기온: { locate.select_one('tmn').string }")
    print(F"최고기온: { locate.select_one('tmx').string }")
    print()