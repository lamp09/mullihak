'''
    작성일 : 2023년 10일 04일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 1. 두 수를 입력받아 두 수 사이의 합계 출력하기.
            2. 두 수 사이의 짝수 합계 출력하기.
            
'''

# 두 수 입력받기
while True :
    num1 = int(input('수 입력 : '))
    num2 = int(input('수 입력 : '))
    if num1 > num2 :
        print('두 번째 수가 첫번째 수보다 작을 수 없습니다..')
        continue

        # 두 수 사이의 합계 구하기
    sum = 0 
    for i in range(num1, num2 + 1):
        sum += i

    # 두 수 사이의 짝수의 합계 구하기
    even = 0
    for i in range(num1, num2 + 1):
        if i % 2 == 0 :
            even += i

    print("두 수 사이의 합계는 {}입니다.".format(sum))
    print("두 수 사이의 짝수의 합계는 {}입니다.".format(even))
    
    stop = int(input("종료를 원하면 0을 입력 :"))
    if stop == 0 :
        break