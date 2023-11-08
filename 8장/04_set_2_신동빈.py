'''
    작성일 : 2023년 11일 08일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 집합의 연산

'''

# 비교 연산자
num1 = {1,2,3}
num2 = {1,2,3}
print(f"num1 == num2 ? {num1 == num2}")

# 6개의 숫자로 집합 생성
num_set = {2,7,9,6,8,2}
print(f"num_set : {num_set}")
print(f"num_set의 길이 : {len(num_set)}")
print(f"num_set 중 가장 큰 값 : {max(num_set)}")
print(f"num_set 중 가장 작은 값 : {min(num_set)}")
print(f"num_set 합 : {sum(num_set)}\n")

num1 = {1,2,3}
num2 = {3,4,5}

# 합집합
print(f"num1 | num2 : {num1 | num2}") # 합집합 연산자 |
print(f"num1.union(num2) : {num1.union(num2)}\n") # 합집합 메소드 union()

# 교집합
print(f"num1 & num2 : {num1 & num2}") # 교집합 연산자 &
print(f"num1.intersection(num2) : {num1.intersection(num2)}\n") # 교집합 메소드 intersection()

# 차집합
print(f"num1 - num2 : {num1 - num2}") # 차집합 연산자 -
print(f"num1.difference(num2) : {num1.difference(num2)}\n") # 차집합 메소드 difference()

# 대칭차집합
print(f"num1 ^ num2 : {num1 ^ num2}") # 대칭차집합 연산자 ^
print(f"num1.symmertric_difference(num2) : {num1.symmetric_difference(num2)}") # 대칭차집합 메소드 symmetric_difference()
