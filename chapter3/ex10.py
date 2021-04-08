import matplotlib.pyplot as plt


figure = plt.figure()
axes = figure.add_subplot(1, 1, 1)

x = [0, 1, 2, 3, 4]
y1 = [4, 1, 3, 5, 2]
y2 = [0, 8, 5, 3, 1]

# plot -> 꺾은선 그래프
# 그래프의 형태나 색상 등 시각적인 부분을 지정할 수 있다.
# linestyle - 선의 형태
# linewidth - 선의 굵기
# color - 선의 색상
# marker - 표시
axes.plot(x, y1, linestyle="dotted", linewidth=5.0)
axes.plot(x, y2, color="r", marker="v")

plt.title("this chart name")
plt.xlabel("day")
plt.ylabel("ranking")
# 최고 순위 - 1, 최저 순위 - 10
# 최고 순위 - 1, 최저 순위 - 200
# plt.axis([1, 31, 0, 200])
plt.axis([1, 31, 0, 200])
plt.show()

'''
figure = plt.figure()
# 첫 번째 매개변수 - 행 번호
# 두 번째 매개변수 - 열 번호
# 세 번째 매개변수 - 차트의 번호
axes1 = figure.add_subplot(1, 2, 1)
axes2 = figure.add_subplot(1, 2, 2)
plt.show()
'''
















