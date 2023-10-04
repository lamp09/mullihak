'''
    작성일 : 2023년 10일 04일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 더하기 암산 문제 만들기
            2개의 수로 더하기 결과를 맞추는 게임.
            2개의 수는 1~100사이 랜덤으로 출제.
            사용자가 0을 입력하면 프로그램은 종료.
            즉, 사용자가 0을 입력하기 전까지는 무한 반복하여 문제 풀기
            정답을 맞추면 " 참 잘했어요!"
            틀리면 정답을 알려주고, " 틀렸습니다." 출력
'''

import random

while True :
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    print("종료를 원하면 0을 입력하시오.")
    print()
    correct = int(input("{} + {} = ".format(num1,num2)))
    if correct == num1 + num2 :
        print("참 잘했어요!")
    elif correct == 0 :
        break
    else :
        print("정답은",num1 + num2,"입니다.")
        print("틀렸습니다.")