#탈출문자
#\n : 줄바꿈
print("백문이 불여일견\n 백견이 불여일타")

#\"\' : 문장 내에서 따옴표
# 나는 "나도코딩" 입니다. 
print("나는 '나도코딩' 입니다.")
print("나는 \"나도코딩\" 입니다")
print("나는 \'나도코딩\' 입니다.")

# \\ : 문장 내에서 \ 
#print("C:\Users\yg990\OneDrive\Desktop\python 연습코드>")
print("C:\\Users\\yg990\\OneDrive\\Desktop\\python 연습코드>")

#\r : 커서를  맨 앞으로 이동
print("Red apple\rPine")


# \b : 백스페이스 (한글자 삭제)
print("Redd\bapple")

# \t : 탭
print("Red\tapple")

# #quiz 3 : 사이트별로 비밀번호를  만들어 주는  프로그램을 작성하시오.
# #규칙1 : http:// 부분은 제외 => naver.com
# #규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# #규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!'로  구성 

address = "http://daum.net"
print("규칙1의 값 :" +address[7:])
address2 = address[7:]
print("규칙2의 값  :" +address2[:address2.find(".")])
address3 = address2[:address2.find(".")]
password = address3[:4] + str(len(address3)) + str(address.count("e")) + "!"
print(f"{address}의 비밀번호 : {password}")

address = "http://naver.com"

a = address[7:12]
A = a[:3]
b = len(a)
c = a.count("e")
print(a,b,c)
print(f" 생성된 비밀번호 : {A}{b}{c}!")


#해답
address = "http://naver.net"
my_str = address.replace("http://", "")
my_str = my_str[:my_str.index(".")]

password = my_str + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{}의 비밀번호는 {}".format(address, password))