# 과제 3

num1 = int(input("첫 번째 양의 정수 입력 :"))
num2 = int(input("두 번째 양의 정수 입력 :"))
num3 = int(input("세 번째 양의 정수 입력 :"))

sum_num = num1+num2+num3

if (num1<0 or num2<0 or num3<0):
    print("양의 정수를 입력하세요.")
else:
    if (sum_num%2==0):
        if (num1 >= num2 and num1 >= num3):
            print(num1)
        elif (num2 >= num1 and num2 >= num3):
            print(num2)
        elif (num3 >= num1 and num3 >= num2):
            print(num3)
    elif(sum_num%2!=0):
        print(sum_num)