'''
작성일 : 2023 09 13 
작성자 : 컴퓨터공학부 202395019 신동빈
 설명 : 터틀사용
'''

import turtle as t  # 터틀 모듈을 사용하기 위해 준비
                    # turtle 클래스 객체를 t로 생성. (별명)


t.speed(6) 
t.shape('turtle')    
# 선그리기
# t.forward(200)
 
# 삼각형 그리기
                    
t.forward(200) # 200px 만큼 이동
t.left(120) # 120px 만큼 회전
t.forward(200) # 200px 만큼 이동
t.left(120) # 120px 만큼 회전
t.forward(200) # 200px 만큼 이동
t.left(120) # 120px 만큼 회전
for y in range(3,10):
    for i in range(y):
        t.forward(200)
        t.left(120)
        t.forward(200)
        t.left(120)
        t.forward(200)
        t.left(120)
t.mainloop()
