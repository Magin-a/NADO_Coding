#튜플 (변경되지 않는 리스트중에서 빠르게 가능 리스트보다 빠르다)
menu = ("돈까스", "치즈까스")
print(menu[0]) #인덱스 값 지정
print(menu[1])

# menu.add("생선까스") #튜플은 값의 변경을 못한다.
# print(menu)
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

#집합 (set) 중복 안됨, 순서없음 
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 (java 와 python  을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python)) # union = 합집합 의미

#차집합 (java  할 수있지만 python은 할줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 까먹음
java.remove("김태호")
print(java)