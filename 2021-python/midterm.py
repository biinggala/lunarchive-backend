import datetime
print("A 항공사 예약시스템")


#매년 새로운 날짜로 수정할 필요가 없도록 날짜(년) 정보를 가져왔습니다.(개선)
this_year = datetime.date.today().year

month31 = [1, 3, 5, 7, 8, 10, 12]
month30 = [4, 6, 9, 11]

#유저의 편의를 위해 생년월일을 한 번에 입력하도록 했습니다.(개선)
birth = input("생년월일 8자리를 입력하세요. :")
year = int(birth[0:4])
month = int(birth[4:6])
day = int(birth[6:8])
id_num = int(birth[2:8])
age = this_year-year

#탑승 가능 여부 확인
if (5<=age<85):
    nation = input("국적을 입력하세요.(in English) :")
    name = input("이름을 입력하세요. :")
    #기내식 제공 여부 확인
    if (12<=age<65):
        #국적 확인
        if (nation=="korea"):
            #이벤트 확인
            if (id_num%9==0):
                print("이벤트 음료가 제공됩니다.")
                print("편안한 여행 되세요.")
            else:
                print("편안한 여행 되세요.")
        else:
            if(id_num%len(name)==0):
                print("이벤트 음료가 제공됩니다.")
                print("편안한 여행 되세요.")
            else:
                print("편안한 여행 되세요.")
                

    else:
        print("기내식이 제공됩니다.")
        if (nation=="korea"):
            if (id_num%9==0):
                print("이벤트 음료가 제공됩니다.")
                print("편안한 여행 되세요.")
            else:
                print("편안한 여행 되세요.")
        else:
            if(id_num%len(name)==0):
                print("이벤트 음료가 제공됩니다.")
                print("편안한 여행 되세요.")
            else:
                print("편안한 여행 되세요.")
        
else:
    print("탑승 제한 연령입니다.")
