#function만 사용해 빌런(villain) 만들기

name="first"
health_first=120
damage_first=0

def attack(health, damage) :
    health = health-damage
    return health

damage_first = attack(health_first, 5)

# second villain
name = "second"
health_second=200
damage_second=0

damage_second = attack(health_second, 10)

# class를 이용해서 function의 제한점 극복

class Enemies :
    def __init__(self, name, health) : # 생성자 << 초기화시키고 싶은 변수 넣기
        self.name = name # 외부 변수 name 값 내부 변수 self.name에 할당
        self.health = health
        self.damage = 0
        pass
    def attack(self, damage) :
        self.health = self.health-damage
        return self.health
    def function_name(self) :  # self 키워드 필요(class 소속 확인용)
        pass
        return 0

first_enemy=Enemies('first', 150) # 자신의 자원(functions과 variables) 확인
second_enemy=Enemies('second', 300) # 자신의 자원(functions과 variables) 확인
pass


