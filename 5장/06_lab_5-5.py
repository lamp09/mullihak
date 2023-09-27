'''
    작성일 : 2023년 9월 27일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 반복문으로 팩토리얼 구하기
'''

num = int(input("수 입력 : "))
fact = 1
for i in range(1, num+1):
    fact = fact*i
    
print(num,"!은",fact,"이다.")