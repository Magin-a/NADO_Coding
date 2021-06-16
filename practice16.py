#클래스
    #일반유닛
class Unit:
    def __init__(self, name, hp, damage): #__init__  객체를 생성할때 자동으로 호출되는 부분
        self.name= name # 멤버변수란 class내에 있는 변수를 칭한다.
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
#marine, tank는 Unit 클래스의 인스턴스라고 한다
#__init__안에 값을 모두 대입해줘야만 돌아간다.
marine1 = Unit("마린", 40, 5)
marine1 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

#레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2))


#메소드
    #공격유닛
class AttackUnit:
    def __init__(self, name, hp, damage): #__init__  클래스로부터 만들어지는 것을 객체
        self.name= name # 멤버변수란 class내에 있는 변수를 칭한다.
        self.hp = hp
        self.damage = damage

    def attack(self, location): #두개의 함수로 나눠져있지만 AttackUnit에 포함이다.
        print("{0}: {1} 방향으로 적군을  공격합니다. [공격력 {2}"\
            .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{} : {} 데미지를  입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되엇습니다".format(self.name))

#메딕



#firebat : 공격유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)