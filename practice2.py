# 간단한 수식
print(2+3*7) #23
print(( 2 + 3 ) * 7 ) #35

number = 2 + 3 * 4 #14
print(number)
number = number + 4 #18
print(number)

number += 2
print(number) # number = number + 2이 식과 같은 방식이다. 20
number *= 3
print(number) # 60
number /=6
print(number) # 10
number -= 2
print(number) #8
number %= 2
print(number) # 나머지0

#숫자 처리 함수
print(abs(-5)) #5
print(pow(4, 2)) #4^2 = 4*4 = 16
print(max(4, 16, -2)) #16
print(min(4, -2, 5)) #-2
print(round(5.12)) #5 반올림
print(round(6.7)) #7

from math import *
print(floor(4.11)) #내림 4
print(ceil(3.7)) #올림 4
print(sqrt(16)) #제곱근 4

#랜덤함수(난수)
from random import *

print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) #0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random()*10)) # 0 ~ 10미만의 임의의 값 생성
print(int(random()*10)+1) #0 ~ 10 이하의 임의의 값 생성

print(int(random()*45)+1) #1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46)) #1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)) #1 ~ 45 이하의 임의의 값 생성 randint(a, b) = 양쪽 끝 a와b 모두 포함하는 랜덤값 생성

# 2일차 Quiz
# 당신은 최근에 코딩 스터디 모임을 새로만들었습니다.
#월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
#아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
#조건1 : 랜덤으로 날짜를 뽑아야 함
#조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로정함
#조건3 : 매월 1~3은 스터디 준비를 해야 하므로 제외

from random import *
a= randint(4, 28)

print("오프라인 스터디 모임 날짜는 매월 "+str(a)+"일로 선정 되었습니다.")
print("오프라인 스터디 모임 날짜는 매월 ",a,"일로 선정 되었습니다.")

#정답
from random import *
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" +str(date)+ "일로 선정되었습니다.")





#"""글꼴 크기 변경
# file > setting > terminal font 
