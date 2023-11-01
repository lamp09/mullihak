'''
    작성일 : 2023년 11일 1일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : LAB7-6 도시의 이름과 인구를 튜플로 묶어보자.
    
           
'''
# 다음과 같은 리스트가 생성되어 있다.
city_info = [('서울',9765),('부산',3441),('인천',2954),('광주',1501),('대전',1531)]

# 최대값과 최솟값, 총합을 변수로 저장
max_pop = 0  # 인구수를 비교했을때 현재 값이 최대 인구수가 될수 있게 하기 위함.
min_pop = 999999999999999999 # 인구수를 비교했을때 현재 값이 최소 인구수가 될 수 있게 하기 위함.
total_pop = 0

# 최대인구 도시와 최소인구 도시를 미지정 상태로 변수에 저장
max_city = None
min_city = None

# city_info 를 city에 넣어 반복
for city in city_info:
    total_pop += city[1] # total_pop에 city[1]번지를 더하기
    if city[1] > max_pop: # 만약 city[1]번지가 max_pop 보다 크다면
        max_pop = city[1] # max_pop에 city[1]번지 저장
        max_city = city # max_city에 city값 저장
    if city[1] < min_pop: # 만약 city[1]번지가 min_pop보다 작다면 
        min_pop = city[1] # min_pop에 city[1]번지 저장
        min_city = city # min_city 에 city값 저장
        

print('최대인구 : {0}, 인구 : {1}천명'.format(max_city[0],max_city[1]))
print('최소인구 : {0}, 인구 : {1}천명'.format(min_city[0],min_city[1]))
print('리스트 도시 평균 인구 : {0}천명'.format(total_pop/len(city_info)))