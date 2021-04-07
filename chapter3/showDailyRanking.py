ranking = []

with open("C:/Users/ITPS/Desktop/app_rank/20210407.tsv", "r", encoding="UTF-8") as file:
    file.readline()

    while True:
        line = file.readline()
        if line == "":
            break

        line = line.split("\t")
        ranking.append(line[0])

start = 0
end = 20

while True:
    for i in range(start, end):
        print("{}. {}".format(i+1, ranking[i]))

    print("[ 1. 다음 순위 ]")
    print("[ 2. 이전 순위 ]")
    print("[ 3. 종료 ]")

    menu = int(input())
    if menu == 1:
        if(start >= 0 & start <200):
            start = start + 20
            end = end + 20
        if start >= 200:
            print("다음 순위가 없습니다!")
            start = start - 20
            end = end - 20
        else:
            print("잘못 입력하셧습니다. 이제 인덱스 값을 초과합니다.")
    elif menu == 2:
        if (start > 0 & start <= 200):
            start = start - 20
            end = end - 20
        else:
            print("잘못 입력하셨습니다. 이제 인덱스 값을 초과합니다.")

        if start < 0:
            print("이전 순위가 없습니다!")
            start = start + 20
            end = end + 20


    else:
        break
















