'''
    작성일 : 2023년 11일 1일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : LAB7-6 도시의 이름과 인구를 튜플로 묶어보자.
    
           
'''
# 다음과 같은 리스트가 생성되어 있다.
city_info = [('서울',9765),('부산',3441),('인천',2954),('광주',1501),('대전',1531)]

# 최대값과 최솟값, 총합을 변수로 저장
max_pop = city_info[0][1]  # 첫 번째 항목이 기준이 됨.
min_pop = city_info[0][1] 
total_pop = 0

# 최대인구 도시와 최소인구 도시를 미지정 상태로 변수에 저장
max_city = city_info[0][0]
min_city = city_info[0][0]

# city_info 를 city에 넣어 반복
for city, pop in city_info:
    total_pop += pop # total_pop에 city[1]번지를 더하기
    if pop > max_pop: # 만약 city[1]번지가 max_pop 보다 크다면
        max_pop = pop # max_pop에 city[1]번지 저장
        max_city = city # max_city에 city값 저장
    if pop < min_pop: # 만약 city[1]번지가 min_pop보다 작다면 
        min_pop = pop # min_pop에 city[1]번지 저장
        min_city = city # min_city 에 city값 저장
        

print('최대인구 : {}, 인구 : {}천명'.format(max_city[0],max_pop))
print('최소인구 : {}, 인구 : {}천명'.format(min_city[0],min_pop))
print('리스트 도시 평균 인구 : {0}천명'.format(total_pop/len(city_info)))