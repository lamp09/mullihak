'''
    작성일 : 2023년 9월 20일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 선택문 if
            성적을 입력 받아 60점 이상이면 "합격입니다."를 출력
'''
# 1. 성적을 입력 받는다 -> 성적을 입력받아(문자) 정수로 변환하여 변수에 저장.
score = int(input("성적 입력 : "))
# 2. 만약 성적이 60점 이상이라면 "합격입니다." 출력
if score >= 60 :
    print("합격입니다.")

'''
자동차의 속도를 입력받아 속도를 출력하고,(현재속도 : 00km/h)
속도가 30km/h이상이면 "과속입니다." 출력
속도와 상관없이 "안전 운전 하세요." 출력
'''

# 1. 속도를 입력받는다.
speed = int(input("속도 입력(km/h) : "))
# 2. 현재 속도를 출력한다.
print("현재속도 : {}km/h".format(speed))
# 3. 만약 속도가 30km/h이상이면 "과속입니다. 속도를 줄이세요." 출력
if speed >= 30 :
    print("과속입니다. 속도를 줄이세요.")
# 4. "안전운전 하세요 출력"
print("안전 운전 하세요.")