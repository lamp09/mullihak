'''
    작성일 : 2023년 11일 1일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 8.1 키와 같은 값을 가지고 딕셔너리

        튜플 = () 리스트 = [] 딕셔너리 = {}
'''
# 빈 딕셔너리 생성 
phone_book1 = {}

# 딕셔너리에 값 저장. 1. key value     [key] = value
phone_book1['신동빈'] = '010 - 4033 - 3143'

print('phone_book1 : ', phone_book1) # {'신동빈': '010 - 4033 - 3143'}

# 딕셔너리에 값 저장. 2. {key : value}
phone_book2 = {'홍길동' : '010-9071-0411', '신동빈' : '010-9750-1280'}

print('phone_book2 : ', phone_book2)

phone_book3 = {}
phone_book3['신동빈'] = '010-9750-1280'
phone_book3['홍승헌'] = '010-9071-0411'
phone_book3['신 혁'] = '010-9731-5262'
phone_book3['황인혁'] = '010-3276-6441'
phone_book3['이동국'] = '010-9753-1284'

print('phone_book3 : ', phone_book3)

print()
print('== 전화번호 phone_book3 출력 ==')

# 모든 key 출력
print(phone_book3.keys()) # .keys 사용하면 모든 key 출력
# 모든 value 출력
print(phone_book3.values())

# 모든 key,value 출력
print(phone_book3.items())

print()
print('== 전화번호 phone_book3 items()출력 ==')
for name,phone_num in phone_book3.items() :
    print(name,':',phone_num)
    
    
print()
print('== 전화번호 phone_book3[key]로 접근하여 출력 ==')
for key in phone_book3.keys():
    print(key,':',phone_book3[key])
    

print()
print('딕셔너리 작성 시 :(콜론)을 기준으로 key:value 작성')
person_dict = {'name' : '신동빈','age' : 19, 'class' : '1학년'}

print('name : ',person_dict['name'])    # 딕셔너리의 'name' 키로 값을 조회하여 출력
print('age : ',person_dict['age'])      # 딕셔너리의 'age' 키로 값을 조회하여 출력
print('class : ',person_dict['class'])

print()

print('== 정렬 ==')
# phone_book3 를 정렬
print(sorted(phone_book3))

print('== 키를 기준으로 전체 정렬 ==')
sorted_phone_book3 =sorted(phone_book3.items(),key = lambda x : x[0])
print(sorted_phone_book3)

print('== 값을 기준으로 전체 정렬 ==')
sorted_phone_book3 =sorted(phone_book3.items(),key = lambda x : x[1])
print(sorted_phone_book3)

print()
print('== 항목 삭제 ==')
del phone_book3['신동빈']
print(phone_book3)

print('== 전체 삭제 ==')
phone_book3.clear()
print(phone_book3)