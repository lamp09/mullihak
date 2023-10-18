'''
    작성일 : 2023년 10일 18일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 도시의 인구 자료에 대한 슬라이싱을 해보자.
    
'''
population =['서울',9725,'부산',3441,'인천',2954]

print('서울 인구 : ',population[1])
print('인천 인구 : ',population[::-1])
step = 2
print('도시 리스트 : ',population[0::step])
print('인구의 합 : ',sum(population[1::step]))