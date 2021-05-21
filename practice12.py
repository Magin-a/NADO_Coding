#가변인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") 
    #print()문을 수행하고 다음꺼를 줄바꿈을 하지않고 이어서 나옴
    print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language): #*language 넣고싶은만큼 넣기가능

    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language: 
        print(lang, end = " ")
    print()   

profile("유재석", 20, "python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin" "Swift")

# #지역변수
# gun = 10

# def checkpoint (soldiers):
#     gun = 20  #이부분에 함수 밖의 gun을 가져오고 싶다면 global gun사용
#     #global gun #전역변수 전역 공간에 있는 gun사용
#     gun = gun - soldiers #여기서의 gun과 함수밖의 gun은 다른기때문에 실행불가
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체총 :{0}".format(gun))
# checkpoint(2) #2명이 경계 근무 나감
# print("남은총 : {0}".format(gun))

# # Quiz 표준 체중을 구하는 프로그램을 작성하시오
# # * 표준 체중 : 각 개인의 키에 적당한 체중
# # (성별에 따른 공식)
# # 남자 키 : 키(m) * 키(m) * 22
# # 여자 키 : 키(m) * 키(m) * 21

# # 조건 1 : 표준 체중은 별도의 함수 내에서 계산
# #          * 함수명 : std_weight
# #          * 전달값 : 키(height), 성별(gender)
# # 조건 2 : 표준 체중은 소수점 둘쨰자리까지 표시

# # (출력 예제)
# # 키 175cm 남자의 표준 체중은 67.38kg 입니다. 

# 나의 답
def std_weight(height, gender):
    if gender == 0:
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height*100, round(height*height*22,2)))
    else :
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height*100, height*height*21))

std_weight(float(input()),int(input()))

#해답
def std_weight(height, gender):
    if gender == '남자':
        return height * height * 22
    else :
        return height * height * 21

height = 175
gender = "남자"
weight = std_weight(height/ 100, gender)
print("키{0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

#해답 변형

def std_weight(height, gender):
    if gender == "남자":
        print("키{0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, round(weight*22, 2)))
    elif gender == "여자":
        print("키{0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, round(weight*21, 2)))


height = float(input("키를 입력하세요 :"))
gender = str(input("성별을 입력하세요 :"))
weight = pow(height/100, 2)
std_weight(height, gender)

