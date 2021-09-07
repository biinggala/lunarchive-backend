session = int(input("수료 학기 입력 :"))
word = " 장학금 수여 대상입니다."

if (1<=session<8):
    score = float(input("평균 학점 입력 :"))
    if (4.0<=score<=4.5):
        print("전액"+word)
    elif (3.5<=score<4.0):
        print("50%"+word)
    elif (3.0<=score<3.5):
        print("30%"+word)
    elif(0<=score<3.0):
        print("장학금 수여 대상이 아닙니다.")
    else:
        print("올바른 성적을 입력하세요.")
        
else:
    print("장학금 수여 대상이 아닙니다.")