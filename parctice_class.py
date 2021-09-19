class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()


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