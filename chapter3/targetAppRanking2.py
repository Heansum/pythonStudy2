from datetime import datetime
import argparse
import calendar
import matplotlib.pyplot as plt

def create_x(t,w,n,d):
    # 리스트 리프리헨션
    return [t*x + w*n for x in range(d)]

def makeRanking(name, start, end):
    # name 앱의 일별 순위
    ranking = []
    for i in range(start, end + 1):
        day = str(i)
        if len(day) == 1:
            day = "0" + day

        today = year + month + day
        rank = 0

        try:
            with open("C:/Users/ITPS/app_rank/" + today + ".tsv", "r", encoding="UTF-8") as file:
                file.readline()

                while True:
                    line = file.readline()
                    if line == "":
                        break

                    line = line.split("\t")
                    rank = rank + 1

                    if line[1].find(name) >= 0:
                        ranking.append(rank)
                        break

            if len(ranking) != i:
                ranking.append(0)
        except FileNotFoundError:
            ranking.append(0)

    return ranking

today = datetime.now()
today = today.strftime("%Y%m")

parser = argparse.ArgumentParser()
parser.add_argument("--name1", type=str, default = None)
parser.add_argument("--name2", type=str, default = None)
parser.add_argument("--date", type=str, default=today)

args = parser.parse_args()
name = args.name
today = args.date

ranking = []

year = int(today[0:4])
month = int(today[4:])
# 해당 년, 월의 1일부터 마지막날까지의 날짜를 구해줌 ! range !
monthrange = calendar.monthrange(year, month)

year = str(year)
month = str(month)
if len(month) == 1:
    month = "0" + month

# 해당월의 첫 째날
start = 1
# 해당 월의 마지막 날
end = monthrange[1]

name1Ranking = makeRanking(name1, start, end)
name2Ranking = makeRanking(name2, start, end)


for i in range(start, end+1):
    day = str(i)
    if len(day) == 1:
        day = "0" + day

    today = year + month + day
    rank = 0

    try:
        with open("C:/Users/ITPS/app_rank/"+today+".tsv", "r", encoding="UTF-8") as file:
            file.readline()

            while True:
                line = file.readline()
                if line == "":
                    break

                line = line.split("\t")
                rank = rank + 1

                if line[1].find(name) >= 0:
                    ranking.append(rank)
                    break

        if len(ranking) != i:
            ranking.append(0)
    except FileNotFoundError:
        ranking.append(0)

dayList = []
for i in range(start, end+1):
    dayList.append(i)

# t -> x축을 구성하는 데이터의 개수
# w -> 한 데이터의 x축의 너비
# n -> n번째 데이터
# d -> y축 데이터의 개수
value_name1_x = create_x(2, 0.8, 1, len(name1Ranking))
value_name2_x = create_x(2, 0.8, 1, len(name2Ranking))

# 막대 그래프
axes = plt.subplot()
axes.bar(dayList, name1Ranking)
axes.bar(dayList, name2Ranking)

middle_x = [(a+b)/2 for(a, b) in zip(value_name1_x, value_name2_x)]
axes.set_xticks(middle_x)
axes.set_xtickslabels(dayList)

plt.plot(dayList, ranking)
plt.xlabel("date")
plt.ylabel("rank")
plt.axis([start, end, 0, 200])
# plt.axis([start, end, 0, 200])
plt.show()
















