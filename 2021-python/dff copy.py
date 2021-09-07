import datetime
print("A 항공사 예약시스템")


#매년 새로운 날짜로 수정할 필요가 없도록 날짜(년) 정보를 가져왔습니다.(개선)
this_year = datetime.date.today().year

#유저의 편의를 위해 생년월일을 한 번에 입력하도록 했습니다.(개선)
birth = input("생년월일 8자리를 입력하세요. :")
id_num = birth[2:8]
year = int(birth[0:4])
month = int(birth[4:6])
day = int(birth[6:8])
age = this_year-year
info1 = "편안한 여행 되세요."
info2 = "잘못된 양식입니다."

month31 = [1, 3, 5, 7, 8, 10, 12]
month30 = [4, 6, 9, 11]


def control():
    if (5<=age<85):
        #기내식 제공 여부 확인
        if (12<=age<65):
                #국적에 따라 이벤트 기준이 다릅니다.
            nation = input("국적을 입력하세요.(In English) :")
            name = input("이름을 입력하세요. :")
            if (nation=="korea"):
                #이벤트 조건을 설정합니다.
                if (int(id_num)%9==0):
                    print("이벤트 음료가 제공됩니다.")
                    print(info1)
                else:
                    print(info1)
            else:
                if(int(id_num)%len(name)==0):
                    print("이벤트 음료가 제공됩니다.")
                    print(info1)
                else:
                    print(info1)
        else:
            print("기내식이 제공됩니다.")
            #국적에 따라 이벤트 기준이 다릅니다.
            nation = input("국적을 입력하세요.(In English) :")
            name = input("이름을 입력하세요. :")
            if (nation=="korea"):
                #이벤트 조건을 설정합니다.
                if (int(id_num)%9==0):
                    print("이벤트 음료가 제공됩니다.")
                    print(info1)
                else:
                    print(info1)
            else:
                if(int(id_num)%len(name)==0):
                    print("이벤트 음료가 제공됩니다.")
                    print(info1)
                else:
                    print(info1)
    else:
        print("탑승 제한 연령입니다.")

#사용자가 보낸 데이터 양식을 확인합니다.(개선)
def check_data():
    #8자리 데이터가 맞는지, 출생년을 알맞게 적었는지 확인합니다.
    if (len(birth)==8 and 1900<year<=this_year):
        #30일까지 있는 달과 31일까지 있는 달, 2월의 경우 조건을 만듭니다.
        if(month in month31):
            if(day>31):
                print(info2)
            else:
                control()
        elif(month in month30):
            if(day>30):
                print(info2)
            else:
                control()
        elif(month == 2):
            if(day>29):
                print(info2)
            else:
                control()
        else:
            print(info2) 
    else:
        print(info2)


check_data()