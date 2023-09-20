'''
    작성일 : 2023년 9월 20일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 선택문 if ~ else 
            random 을 이용한 가위바위보 게임.
            
            random함수로 생성된 정수를 가지고 게임을 진행합니다.
            0 => 가위
            1 => 바위
            2 => 보
            
            두 명의 플레이어의 이름을 입력 받아
            가위바위보 게임을 진행합니다.
'''
# random 함수 가져오기.
import random

p1 = input("플레이어 이름 입력 : ")
p2 = input("플레이어 이름 입력 : ")
 
# 무작위로 0,1,2 생성
num1 = random.randrange(3)
num2 = random.randrange(3)
# 가위 바위 보 출력
print(f"{p1} : ", end='')
if num1 == 0 :
    print("가위")
elif num1 == 1 :
    print("바위")
else :
    print("보")

print(f"{p2} : ", end='')
if num2 == 0 :
    print("가위")
elif num2 == 1 :
    print("바위")
else :
    print("보")
    
if ((num2 == 0 and num1 == 1) or (num2 == 2 and num1 == 0) or (num2 == 1 and num1 == 2))  :
    print(f'{p1} WIN!')
elif ((num1 == 0 and num2 == 1) or (num1 == 2 and num2 == 0) or (num1 == 1 and num2 == 2)) :
    print(f'{p2} WIN!')
else : 
    print('DRAW!')