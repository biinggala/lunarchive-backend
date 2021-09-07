
'''
-20 ~ 20 사이의 랜덤한 10개의 수로 이루어진 리스트를 구현하고 (0 제외)
값의 범위를 8개씩 끊어 5개의 상태를 각각의 상태를 -20부터 'sad' 'happy' 'angry' 'mad' 'good'로 지정한다.
이후 사용자가 어떠한 값을 입력하였을때
값이 없다면 [Value X] 와 'chaos' 라는 문자열을 출력하고
값이 존재한다면 입력한 값이 위치한 주소값 즉, Index='n' 과
위 범위를 slice하여 지정한 상태를 같이 출력하도록 한다.

위 과정을 총 happy의 상태가 2번 angry의 상태가 1번 나올때 까지 반복하며 (나머지 상태는 반복횟수에 관여하지 않음)
조건을 만족하여 종료하는 경우 가장 많이 뽑힌 상태를 최종적으로 출력하시오.
'''

import random

pre_list = []

def make_list():# 랜덤한 10개의 리스트를 만드는 함수입니다.
    user_num = int(input("input:"))
    pre_list.clear()#나중에 for 문에서 리스트가 무한정 늘어나지 않게 clear을 사용합니다
    for i in range(-20, 21):#랜덤한 값 리스트를 만들기 위해 범위를 지정합니다.
        if (i==0):
            pass
        else:
            pre_list.append(i)
    num_list = random.sample(pre_list,10)#-20~20 사이 랜덤한 10개의 숫자 리스트 만듭니다.
    check_statement(num_list, user_num)

state = {'sad':0, 'happy':0, 'angry':0, 'mad':0, 'good':0}

def check_statement(list, num):#input값과 생성된 리스트를 대조하는 함수입니다.
    print(list)
    if (num in list):#입력한 숫자가 리스트에 있는지 확인합니다.
        index = list.index(num)
        if (num in pre_list[0:8]):
            print(f'index={index}',"sad")
            state['sad']=state['sad']+1#state 딕셔너리의 값을 변경합니다.

        elif (num in pre_list[8:16]):
            print(f'index={index}',"happy")
            state['happy']=state['happy']+1
            
        elif(num in pre_list[16:24]):
            print(f'index={index}',"angry")
            state['angry']=state['angry']+1

        elif(num in pre_list[24:32]):
            print(f'index={index}',"mad")
            state['mad']=state['mad']+1

        elif(num in pre_list[32:40]):
            print(f'index={index}',"good")
            state['good']=state['good']+1
    else:
        print([num],'chaos')

def excute():#위의 과정을 특정 조건이 나올 때까지 반복시키는 함수입니다.
    while True:
        make_list()
        if (state['happy'] == 2) and (state['angry'] == 1):
            max_key = max(state, key=state.get)#value가 가장 큰 key를 찾습니다.
            print(f'Today is {max_key}')
            break
            
excute()