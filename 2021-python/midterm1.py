import datetime
print("A 항공사 예약시스템")


#매년 새로운 날짜로 수정할 필요가 없도록 년도를 가져왔습니다.
this_year = datetime.date.today().year

month31 = [1, 3, 5, 7, 8, 10, 12]
month30 = [4, 6, 9, 11]


#유저가 입력한 값이 형식에 맞는지 확인합니다.
def date_check():
    #유저의 편의를 위해 생년월일을 한 번에 입력하도록 했습니다.
    id_num = input("생년월일 8자리를 입력하세요. :")
    id_year = int(id_num[0:4])
    id_month = int(id_num[4:6])
    id_day = int(id_num[6:8])
    if (len(id_num)==8 and id_year<=this_year):
        if(id_month in month31):
            if(id_day>31):
                print("다시 입력해주세요.")
            else:
                age_check()
        elif(id_month in month30):
            if(id_day>30):
                print("다시 입력해주세요.")
            else:
                age_check()
        elif(id_month == 2):
            if(id_day>29):
                print("다시 입력해주세요.")
            else:
                age_check()
        else:
            print("다시 입력해주세요.") 
    else:
        print("다시 입력해주세요.")
        

def age_check():
    pass


def event_check():
    pass

def free_check():
    if (5<age_info<85):
        if (age_info<12 or age_info>=65):
            print("기내식을 무료로 제공해드립니다.")
            input("내국인/외국인 :")

    else:
        print("탑승이 불가합니다.")

date_check()

