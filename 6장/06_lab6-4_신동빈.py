'''
    작성일 : 2023년 10일 11일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : LAB 6-4 리스트에서 최대값, 최소값을 찾아 돌려주는 함수.
    
    리스트 10개의 값을 랜덤으로 생성하고,
    max 또는 min을 입력 받아 최대,최소값을 찾아 돌려주는 함수.

    (함수)
            5) 두 값을 전달받아 매개 변수에 저장
            6) 최댓값,최솟값을 찾는다.
            7) 값을 돌려준다.
    (메인)
        1. 무한 반복
            1) 랜덤으로 10~99까지 10개의 수를 리스트로 생성
            2) 생성된 리스트를 출력
            3) 사용자로부터 최댓값 혹은 최솟값을 알고 싶은지 묻는다.
                이때, 사용자가 입력해야 될 값은 max or min 이다.
            4) 입력받은 max 또는 min과 생성된 리스트를 가지고 함수 호출
            8) 돌려받은 최댓값 또는 최솟값을 출력한다.
'''
from random import randint

def getmaxmin(lab_list, maxmin):
    return max(lab_list) if maxmin =='max' else min(lab_list)
while True :
    lab_list = []
    for i in range(10):
        lab_list.append(randint(10,99))
    print(lab_list)
    maxmin = input("최댓값 or 최솟값(max 또는 min 으로 입력) = ")
    if maxmin == ['max','min'] :
        continue
    print("{}값은 {}입니다.".format(maxmin,getmaxmin(lab_list,maxmin)))
    