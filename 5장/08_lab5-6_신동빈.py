'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395019 신동빈
    설명 : 사용자로부터 암호를 입력 받아 로그인하기
            교재 128p
            
            사용지로부터 계속해서 암호를 입력 받는다.
            암호가 맞으면 "로그인 성공" 메세지를 출력한다.
            암호가 맞을 때까지 반복한다.
            암호는 1234
            
            암호가 1234가 아니면 계속 암호를 입력하라고 한다.
'''

pwd = ""

while pwd != "1234" :
    pwd = input("암호를 입력하세요 : ")

print("로그인 성공")