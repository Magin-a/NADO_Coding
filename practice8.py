    #자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))  #리스트

menu = tuple(menu)
print(menu, type(menu))  #튜플 

menu = set(menu)
print(menu, type(menu)) #set

# Quiz 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓슬 이벤트를 진행하기로 하였습니다.
# 댓슬 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰으 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는  1~20이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
# --- 당첨자 발표 ---
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# --- 축하합니다 ---

# # (활용예제)
# from random import *
# 1st = [1, 2, 3, 4, 5]
# print(1st)
# shuffle(1st)
# print(1st)
# print(sample(1st, 1))

from random import *
my_list = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(my_list)
print(sample, 4)

print("축하드립니다."+ str(sample(my_list, 1)+ "치킨 당첨 입니다."))
# del my_list (sample(my_list, 1))

print(sample(my_list, 3))
print("축하드립니다."+str(sample(my_list, 3)+ "커피 당첨 입니다."))


#나의 코딩에서 수정한 답
from random import *
my_list = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

shuffle(my_list)

student = sample(my_list, 4)
print(f"당첨을 축하드립니다. {student[0]} 치킨 당첨 입니다.")
print(f"당첨을 축하드립니다. {student[1:]} 커피 당첨 입니다.")



#정답
from random import *
users = range(1, 21) #1부터 20까지 생성
users = list(users)

shuffle(users)
print(users)

winners = sample(users, 4) #4명중에서 1명은 치킨, 3명은 커피
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("---당첨을 축하드립니다.---")

