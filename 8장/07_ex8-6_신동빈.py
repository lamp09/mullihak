'''
    작성일 : 2023년 11일 08일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 튜플을 요소로 가지는 student_tup 리스트가 있다. 이 튜플의 요소가 되는 튜플은 (학번,이름,전화번호)로 구성되어있다.
            (1) 이를 이용하여(학번:이름)의 딕셔너리를 만들어 출력하시오.
            (2) 이를 이용하여 학번으로 조회할 경우 학번, 이름과 전화번호를 출력되도록 하여라.
'''

student_tup = [('211101','조성훈','010-1234-4500'), ('211102', '김은지','010-2230-6540'), ('211103','윤소정','010-3232-7788')]
dict1 ={}

for i in student_tup :
    dict1[i[0]] = i[1]
    
for key, value in dict1.items() :
    print(f"{key} : {value}")
student_tup = tuple(student_tup)
input_school_num = input("학번 입력 : ")
num = 0
for i in student_tup :
    if input_school_num in i:
        break
    num += 1
    
print(f"{input_school_num} 학생은 {student_tup[num][1]}이며, 전화번호는 {student_tup[num][2]}입니다.")    