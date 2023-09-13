'''
작성일 : 2023 09 13 
작성자 : 컴퓨터공학부 202395019 신동빈
 설명 : 90페이지 문제 3.9
    평균 시속과 이동시간을 입력받아
    이동시간은 시, 분,초 단위로 출력하고, 
    이동한 거리를 계산하여 출력하시오.
    
'''

#1. 평균 시속 이동시간 입력
speed = float(input('평균 시속(k/h) : '))
time = float(input('이동시간초 : '))
# 2. 이동 시간 계산 
hour = time // 1
min = (((time-hour)*3600)//60)
sec = int(((time-hour))*3600)%60
# 3. 출력
print('평균 시속 : {}km/h'.format(speed))
print('이동 시간 : {:.0f}시간 {:.0f}분 {}초'.format(hour, min, sec))
print('이동거리 : {}km'.format(speed * time))