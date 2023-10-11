'''
    작성일 : 2023년 10일 11일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 여러개의 값을 넘겨주고 여러개의 값을 돌려받기.
    
    두 수를 전달하여 사칙연산의 결과값을 출력한다.
    
    [알고리즘]
    (함수)
        1. 두 수를 입력받아 매개 변수에 저장한다.
        2. 두 수의 사칙연산을 계산한다.
        3. 두 수의 사칙연산의 결과를 모두 돌려준다.
    (메인)
        1. 두 수를 입력받는다.
        2. 두 수를 가지고 함수를 호출하고 돌려받은 값을 바로 출력한다.
'''

def cals(num1,num2):
    sum = num1 + num2
    minus = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    rest = num1 % num2
    return sum, minus, mul, div, rest

num1 = int(input("수 입력 : "))
num2 = int(input("수 입력 : "))

sum, minus, mul, div, rest = cals(num1,num2)
print(f"{num1} + {num2} = {sum}")
print(f"{num1} - {num2} = {minus}")
print(f"{num1} * {num2} = {mul}")
print(f"{num1} / {num2} = {div}")
print(f"{num1} % {num2} = {rest}")