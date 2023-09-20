'''
    작성일 : 2023년 9월 20일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 선택문 if ~ else 
            정수를 입력받아 짝수, 홀수는 양수일 경우에만 판단한다.
            짝수 = 2로 나눈 나머지가 0이다. 
            홀수 = 2로 나눈 나머지가 1이다.
'''
#1 . 정수를 입력 받는다.
num = int(input("정수 입력 : "))
# 2. 만약 정수가 양수라면
if num > 0 :
#   1) 만약 num이 2로 나누었을때 나머지가 0이면 짝수라 판단
    if num % 2 == 0 :
        print(" {}은 짝수입니다.".format(num))
#   2) 아니면 홀수라 판단
    else :
        print("{}은홀수입니다.".format(num))
else :
    print(f"{num}음수입니다.")