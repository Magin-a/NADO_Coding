#사전(딕셔러니)
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

print(cabinet[5])       #오류가 나고 프로그램 종료  []
print(cabinet.get(5))   #get 사용시 프로그램이 종료하지 않고 계속 이어감
print(cabinet.get(5, "사용 가능")) # 5라는 값이 없어서 '사용가능' 입력값을 출력한다.
print("hi")

print(3 in cabinet) #True
print(5 in cabinet) #False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.value())

# key, value 쌍으로 출력
print(cabinet.item())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)