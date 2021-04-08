import random

ranking = []

with open("C:/Users/ITPS/Desktop/app_rank/20210407.tsv", "r", encoding="UTF-8") as file:
    label = file.readline()

    while True:
        data = file.readline()
        if data == "":
            break

        print(data)
        ranking.append(data)

random.shuffle(ranking)

with open("C:/Users/ITPS/Desktop/app_rank/20210401.tsv", "w", encoding="UTF-8") as file:
    file.write(label)

    for rank in ranking:
        file.write(rank)
















