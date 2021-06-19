#스타크래프트게임
from random import *
class Unit: #상속하는 유닛 부모 클래스
    def __init__(self, name, hp, speed): #__init__  클래스로부터 만들어지는 것을 객체
        self.name= name # 멤버변수란 class내에 있는 변수를 칭한다.
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성됐습니다.".format(self.name))

    def move(self, location):
        
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{} : {} 데미지를  입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되엇습니다".format(self.name))


    #공격유닛
class AttackUnit(Unit): #상속받는 자식클래스
    def __init__(self, name, hp, speed, damage): 
        Unit.__init__(self, name,hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0}: {1} 방향으로 적군을  공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
        
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

        #스팀팩: 일정 시간 동안 이동 및 공격속도 증가
    def stimpack(self):
        if self.hp >10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않았습니다. ".format(self.name))

class Tank(AttackUnit):
    seize_developed = False
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        #시즈모드 실행
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2 
            self.seize_mode = True
        #시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2 
            self.seize_mode = False


class Flyable:
    def __init__(self, flying_speed):
         self.flying_speed = flying_speed

    def fly(self, name,location):
        print("{0} : {1} 방향으로 날았습니다. [ 속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable): #다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self,name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location): #지상유닛 클래스에서는 move가 정의 되어있지만 모두 통일되게 사용하기 위해서 재 정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
    

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False #클로킹모드 (해제상태)

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else :# 클로킹 모드 해제 -> 모드설정
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로우 게임을 시작합니다.")

def game_over():
    print("player : gg")
    print("[player] 님이 게임에서 퇴장하셨습니다.")

#실제 게임 시작
game_start()
m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

#유닛일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move("1시")

#탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었스비다.")

#공격 모드 준비(마린 : 스팀패그 탱크 : 시즈모드, 레이스 :클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

#전군 공격 
for unit in attack_units:
    unit.attack("1시")

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21))

# 게임 종료
game_over()
