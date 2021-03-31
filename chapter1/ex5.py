try:
    filename = input('열고자 하는 파일명을 입력하세요 >>>')
    file = open(filename, 'r')

    print("파일이 열렸음")
except FileNotFoundError:
    print("파일이 존재하지 않음")
else:
    file.write("파일에 내용 저장")
finally:
    file.close()



