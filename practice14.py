#파일 입출력
score_file = open("score", "w", encoding="utf8")  #open(파일명, "w=쓰기목적",- )
print("수학 : 0", file=score_file)
print("영어 : 0", file=score_file)
score_file.close()


score_file = open("score", "a", encoding="utf8") #a는 append약자
score_file.write("과학 : 80")
score_file.write("\t코딩 : 80")  #write는 줄바꿈을 자동으로 안해준다
score_file.close()

# #읽기
# score_file = open("score", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

#한줄씩 읽어오기
score_file = open("score", "r", encoding="utf8")
print(score_file.readline()) #줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
x = score_file.strip()

#파일의 내용이 몇줄짜이인지 모를 때 반복문을 통해서 
score_file = open("score", "r", encoding="utf8")
while True:
    line = score_file.readline() #한줄씩 라인을 불러옴
    if not line: # 라인에 내용이 없다면?
        break
    print(line, end= "") #end= "" 줄바꿈을 하지 않는다
score_file.close()

#리스트에 값을 넣고 
score_file = open("score", "r", encoding="utf8")
lines = score_file.readlines() #list 형태로 저장
print(lines)
for line in lines:
    print(line, end="")

score_file.close()