# #함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")



def desposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다".format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
        return (balance - money)
    else :
         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
         return balance

def withdraw_night(balance, money): #저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0 #잔액
balance = desposit(balance, int(input()))
print(balance)

balance = withdraw(balance, 5000)
print(balance)

commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))


#기본값
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang)) #\ + enter 는 줄바꿈으로 이어줌

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

#같은 학교 같은 학년 같은 반 같은수업.

def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))

profile("유재석")
profile("김태호")

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")