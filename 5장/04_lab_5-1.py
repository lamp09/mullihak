'''
    작성일 : 2023년 9월 27일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 터틀 그래픽으로 여러개의 원을 그려보자
'''

import turtle
t = turtle.Turtle()
t.speed(10)
# 원 하나 그리기
# t.circle(100)
for count in range(10):
    t.circle(100)
    t.left(60)
    
t.mainloop()