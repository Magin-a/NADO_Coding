#문자열
sentence = '나는 소년이다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""   # """"이는 줄바꿈을 하여도 문자열을 인식 해준다.            
print(sentence3)

#슬라이싱
jumin = "990828-1235467"  #자릿수는 처음이 0부터시작

print(" 성별 : " + jumin[7]) 
print(" 연 : " + jumin[0:2]) #[]안에서 정의한 값에서 0부터 2 직전까지(99)
print(" 월 : " + jumin[2:4])
print(" 일 : " + jumin[4:6])

print("생년월일 :" + jumin[:6]) #처음부터 6째자리 직전까지
print("뒤 7자리 :" + jumin[7:]) #7째자리부터 끝까지
print("뒤 7자리 뒤에부터 :" + jumin[-7:])

#문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) #[]안에 있는 n번째자리가 대문자인가의 대한 True/False 
print(len(python)) #len()안의 값의 문자여르이 총 길이
print(python.replace("Python", "Java")) #replace(a,b) a를 b로 바꾼다.

index = python.index("y") #python 문자열 중에 "n"은 몇번째에 있는가
print(index) 
index = python.index("n", index + 1) #앞에 저의된 index값에서 index("찾는 값", 시작 위치)
print(index)

print(python.find("Java")) #값이 없을 경우 -1을 출력한다
#print(python.index("Java")) 하지만 index는 오류가 뜬다.
print(python.count("n")) # "n"이 등장한 갯수 값을 출력

#문자열 포맷
#ex) 기존의 문자열 포맷  
# print("a" + "b")
# #print("a", "b")

#방법1
print("나는 %d살 입니다." % 20) # d는 정수 
print("나는 %s을 좋아합니다" % "파이썬")# s(str)는 문자열
print("Apple은 %c로 시작합니다." % "A") # c 캐릭터 문자 하나
# %s 이거 하나로도 실행가능
print("나는 %s 살 입니다." % 20)

print("나는 %s색과 %s 색을 좋아합니다." % ("파란", "빨강"))

#방법2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아합니다.".format("파랑", "빨강"))
print("나는 {1}색과 {0}색을 좋아합니다.".format("파랑", "빨강"))#.foramt("a","b") 0번째 {}에 첫번째인 파랑 1번째 {}에 빨강이 들어간다

#방법3
print("나는 {age}살이며, {color}색을 좋아합니다.".format(age = 10, color = "빨강"))

#방법4 (v3.6이상 ~)
age = 15
color = "파랑"
print(f"나는 {age}살이고, {color}색을 좋아합니다")