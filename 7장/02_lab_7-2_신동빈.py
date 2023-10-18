'''
    작성일 : 2023년 10일 18일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 입력을 받아 맛있는 과일의 리스트를 만들자.
    
    좋아하는 과일 5개를 입력 받아 리스트에 저장한다.
    과일 이름을 입력하여 해당 과일이 리스트에 있는지 없는지 판단.
    
    추가 = append() 메소드
    찾기 = in 연산자

'''
# 빈 리스트 생성
fruits = []

# 5번 반복하여 과일을 입력받아 리스트에 저장
for i in range(5):
    fruit = input('좋아하는 과일 입력 : ')
    fruits.append(fruit)
print(fruits)

# 찾고자 하는 과일을 저장
check = input('찾고자 하는 과일 입력 : ')

# 찾고자 하는 과일을 찾고 출력 
if check in fruits :
    print(f'찾고자 하는 과일인 {check}가 있습니다.')
else :
    print(f'찾고자 하는 과일인 {check}가 없습니다.')