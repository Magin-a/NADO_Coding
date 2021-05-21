#조건 if
weather = input("오늘 날씨는 어때요?")
if weather == "미비" :
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else :
    print("준비물이 필요 없어요.")

temp = int(input("기온은 어때요?"))
if 30<= temp:
    print("너무 더워요. 나가지 마세요.")
elif 10<= temp and temp <30 :
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else :
    print("너무 추어워요. 나가지 마세요.")


#for
print("대기번호 : 1")
print("대기번호 : 4")

for waiting_no in  [0, 1 ,2 , 3, 4]:
    print("대기번호 :{}".format(waiting_no))

for waiting_no in range(1, 6): #  1, 2, 3, 4, 5
    print("대기번호 :{}".format(waiting_no))


starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{}, 커피가 준비되었습니다.".format(customer))  

#while문
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")
    
customer = "아이언맨"
index = 0
while True:
    print("{0}, 커피가 준비 되었습니다. 호풀 {1}회".format(customer, index))
    index += 1

#ex1
customer = "토르"
person = "Unknown"

while person != customer :
    print("{0} 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")

    if person == customer :
        print(" 맛있게 드세요.")
