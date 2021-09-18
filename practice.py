# # # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음.
# # name = "마린" #유닛의 이름
# # hp = 40 #유닛의 체력
# # damage = 5 #유닛의 공격력

# # print("{0} 유닛이 생성되었습니다.".format(name))
# # print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # # 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반모드/시즈모드.
# # tank_name = "탱크"
# # tank_hp = 150
# # tank_damage = 35

# # print("{0} 유닛이 생성되었습니다.".format(tank_name))
# # print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# # tank2_name = "탱크"
# # tank2_hp = 150
# # tank2_damage = 35

# # print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# # print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# # def attack(name, location, damage):
# #     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력, {2}]".format(\
# #         name, location, damage))

# # attack(name, "1시", damage)
# # attack(tank_name, "1시", tank_damage)
# # attack(tank2_name, "1시", tank2_damage)

# # class Unit:
# #     def __init__(self, name, hp, damage):
# #         self.name = name
# #         self.hp = hp
# #         self.damage = damage
# #         print("{0} 유닛이 생성되었습니다.".format(self.name))
# #         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# # marine1 = Unit("마린", 40, 5)
# # marine2 = Unit("마린", 40, 5)
# # tank = Unit("탱크", 150, 35)

# # wraith1 = Unit("레이스", 80, 5)
# # print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# # wraith2 = Unit("빼앗은 레이스", 80, 5)
# # wraith2.clocking = True

# # if wraith2.clocking == True:
# #     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
# from random import*

# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     #stimpack : 일정 시간동안 이동 및 공격 속도를 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp>10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스탬팩을 사용하지 않습니다.".format(self.name))

# # 탱크
# class Tank(AttackUnit):
#         # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 공격력으로 공격 가능, 이동 불가
#     seize_developed = False

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return

#         # 현재 시즈모드가 아닐 때 -> 시즈모드
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         # 현재 시즈모드일 때 -> 시즈모드 해제
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False

    


# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]"\
#             .format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) #지상 스피드 : 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False #클로킹 모드(해제상태)

#     def clocking(self):
#         if self.clocked == True: #클로킹 모드 -> 모드 해제
#             print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
#             self.clocked == False
#         else: #클로킹모드 해제 -> 설정
#             print("{0} : 클로킹 모드를 설정 합니다.".format(self.name))
#             self.clocked = True

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg")
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")


# # 게임 시작
# game_start()

# #유닛 생성 (마린 3, 탱크 2, 레이스 1)
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# t1 = Tank()
# t2 = Tank()

# w1 = Wraith()

# # 유닛 일괄 관리 (생성된 모든 유닛 append)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# # 탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# # 공격 준비 (마린 : 스팀팩, 탱크 : 시즈, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 21)) # 공격은 랜덤으로 받음 (5~ 20)

# # 게임 종료
# game_over()

# Quiz)

# 출력예제
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]


#나

# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_yaer = completion_year

#     #매물 정보 표시
#     def show_detail(self):
#         print("{0} {1} {2} {3} {4}"\
#             .format(self.location, self.house_type, self.deal_type,\
#                  self.price, self.completion_yaer))

# h1 = House("강남", "아파트", "매매", "10억", "2010년")
# h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# h3 = House("송파", "빌라", "월세", "500/50", "2000년")
# 매물들 = [h1, h2, h3]
# print("총 3대의 매물이 있습니다.")
# for i in 매물들:
#     House.show_detail(i)
    
#    House.show_detail(i) == i.show_detail() 참고할 것

#유튜바

# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_yaer = completion_year

#     #매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type,\
#                  self.price, self.completion_yaer)

# houses = []
# h1 = House("강남", "아파트", "매매", "10억", "2010년")
# h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# h3 = House("송파", "빌라", "월세", "500/50", "2000년")
# houses.append(h1)
# houses.append(h2)
# houses.append(h3)

# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()
