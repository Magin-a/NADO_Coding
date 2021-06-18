class Unit:
    def __init__(self):
        print("Unit 생성장")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__() #다중상속시 위 클래스중 가장 마지막 것만 상속한다

dropship = FlyableUnit()