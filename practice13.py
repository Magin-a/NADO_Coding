print("Python", "java", "Javascript", sep=" vs ")
print("Python", "java", "Javascript", sep=" , ")
print("Python", "java", "Javascript", sep=",", end = " ")
print("무엇이 더 재밌을까요?")

import sys  
print("Python", "java", file=sys.stdout)
print("Python", "java", file=sys.stderr)

scores = {"수학": 0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") #.ljust 왼쪽정렬


#은행 대기순번표
#001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : "+ str(num).zfill(3)) #zfill은 공간 3만큼 확보하고 빈공간을 0으로 채워준다

answer = input("아무 값이나 입력하세요 :")
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")
#사용자 입력을 통해서 나온값은 문자열 형태로 저장이 된다



# #다양한 출력 포맷

# #빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))

# 양수일 떈 +로 표시 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸을 -로 채움
print("{0:_<+10}".format(500))
# 3자리 마다 콤마를 찍어주기 +-부호 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(100000000000))
#3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
#돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
print("{0:^<+,}".format(100000000000))
#소수점 출력
print("{0:f}".format(5/3))
#소수점 특정 자리수 까지만 표시 나머지는 반올림
print("{0:2f}".format(5/3))