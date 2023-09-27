'''
    작성일 : 2023년 9월 27일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 점수를 입력받아 학점을 출력하시오.
            90 ~ 100 : A학점
            80 ~ 89 : B학점
            70 ~ 79 : C학점
            60 ~ 69 : D학점
            0 ~ 59 : F학점
'''
# 1. 점수를 입력받는다.

score = int(input("점수 입력 : "))

# 2. 학점을 계산하여 출력한다.
if 90 <= score < 101 :
    print("A학점입니다.")
elif 80 <= score <= 89 :
    print("B학점입니다.")
elif 70 <= score <= 79 :
    print("C학점입니다.")
elif 60 <= score <= 69 :
    print("D학점입니다.")
else : 
    print("F학점입니다.")
    
    
# 정확한 범위를 지정하자. - 성적의 범위를 벗어나면 잘못된 점수 입력입니다.

print("::: 첫 번째 성적처리 :::")

if (90<=score<=100):
    print("A학점")
elif (80<=score<=89):
    print("B학점")
elif (70<=score<=79):
    print("C학점")
elif (60<=score<=69):
   print("D학점") 
elif (0<=score<=59):
    print("F학점")
else :
    print("잘못된 점수 입력입니다.")
    
    
# 점수는 무조건 0 ~ 100 점 사이. - 아니면 잘못된 입력입니다. 
print("::: 세 번째 성적처리 :::")
if 0 <= score <= 100 :
    if 90 <= score < 101 :
        print("A학점입니다.")
    elif 80 <= score <= 89 :
        print("B학점입니다.")
    elif 70 <= score <= 79 :
        print("C학점입니다.")
    elif 60 <= score <= 69 :
        print("D학점입니다.")
    else :  # a,b,c,d 학점이 아니면
        print("F학점입니다.")
else :  # 0~100사이 점수가 아니면
    print("점수를 잘못 입력하셨습니다.")