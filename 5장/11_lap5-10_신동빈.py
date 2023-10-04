'''
    작성일 : 2023년 10일 04일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 사용자가 입력하는 숫자의 합
    교재 133 페이지
'''

sum = 0 
answer = 'y'
while True :

    num = int(input("수 입력 : "))
    sum += num
    answer = input("계속하시겠습니까?(y/n) : ")
    if answer == 'n' :
        break

print("숫자의 합 : {}".format(sum))