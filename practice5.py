# 리스트  []

#지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가  다음 정류장에서 다음칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석씨/조세호씨 사이에 태워봄
subway.insert(1, "정현돈") # .insert(위치, 값)
print(subway)

#지하철에 있는 사람을  한명씩 뒤에서 꺼냄
print(subway.pop(0))
print(subway)

#같은 이름의 사람이 몇명이 있는지  확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5, 4, 3, 2, 1]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함꼐 사용
mix_list = ['조세호', 5, 3.14]
print(mix_list)

#리스트 확장
num_list= [1, 2, 3, 4]
num_list.extend(mix_list)
print(num_list)