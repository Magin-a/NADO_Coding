import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미": ["축구","골프","코딩"]}
print(profile)
pickle.dump(profile, profile_file) #profile에 있는 정보를 file 에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb") 
profile = pickle.load(profile_file) #file 에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

#with
import pickle

with open("profile.pickle", "rb") as profile_file: # with (파일)을 열어서 as (변수)로 저장
    print(pickle.load(profile_file)) # profile_file을  pickle.load해서 프린트 함

#닫아줄 필요없이 with 탈출시 자동으로 닫아줌

with open("study.txt", "w", encoding="uft8") as  study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


#강의 7번째 퀴즈
#quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
#보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
# - X주차 주간보고 - 
#부서 :
#이름 :
#업무 요약 : 
#1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
#조건 : 파일명은 'X주차.txt'와 같이 만듭니다.

#나의 해답
import pickle

x = int(input("몇주차 보고서를 만들까요 :"))
with open(str(x)+"주차.txt", "w", encoding="utf8") as study_file:
    study_file.write("-"+str(x)+"주차 주간보고-")
    study_file.write("\n부서 :")
    study_file.write("\n이름 :")
    study_file.write("\n업무 요약 :")

#강의 해답
for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        study_file.write("-{0}주차 주간보고-".format(i))
        study_file.write("\n부서 :")
        study_file.write("\n이름 :")
        study_file.write("\n업무 요약 :")