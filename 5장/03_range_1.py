'''
    작성일 : 2023년 9월 27일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : range() 함수
'''
for i in range(3): # i 변수에 0~2의 값이 저장 됨.
    print(i,end='. ')
    print("안녕하세요.")
    print("    신동빈입니다.")
    
# range(시작값, 숫자 앞까지, 증가값(감소값))
#c언어 -> for(초기값; 조건식; 증감식)

for i in range(1,6):    # range(1,6,1)
    print(i,end=' ')
    
# 10에서 1까지 출력
for i in range(10,0,-1):
    print(i,end=' ')