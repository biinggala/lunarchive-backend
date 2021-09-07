# 과제 1

import random#주사위 랜덤 숫자


for i in range(7):#7번 반복
    machine = random.randint(1,6)#random class 사용
    human = random.randint(1,6)
    result = print(f"machine:{machine}, human:{human}")

    if (machine>human):
        print("You Lose")
        result
    elif (machine == human):
        print("Draw")
        result
    else:
        print("You Win")
        result
        
