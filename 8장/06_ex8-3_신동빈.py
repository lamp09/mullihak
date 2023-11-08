'''
    작성일 : 2023년 11일 08일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 학번, 이름 , 전화번호 3쌍의 요소를 가지는 student_tup라는 튜플이 존재한다.
            (1) student_tup 를 수정하여 {학번 : ['이름', '전화번호']}의 쌍으로 이루어진 딕셔너리를 만들어서 출력하라.
            (2) 이 정보를 이용하여 학생의 학번을 입력으로 받아서 이름과 전화번호를 출력하는 학사정보 프로그램을 작성하라.
            (3) student_tup의 마지막 항목으로 직전학기의 학점을 추가하라. 이 정보를 바탕으로 딕셔너리를 만들어서 학생 정보 출력하라.
            (4) 학생의 학점 평균을 출력하라.
'''

student_tup = (('211101','조성훈','010-1234-4500'), ('211102', '김은지','010-2230-6540'), ('211103','윤소정','010-3232-7788'))
dict1 ={}

for school_num, name, number in student_tup :
    dict1[school_num] = [name, number]


print("== 학생 정보 목록 ==")
for key, value in dict1.items() :
    print("{" + "\'{}\' : {}".format(key, value)+"}" )

input_school = input ("학번을 입력 : ")
print("이름 : ",dict1[input_school][0])
print("연락처 : ", dict1[input_school][1])

num = sum = 0
student_tup =list(student_tup)
'''
for i in student_tup :
    student_tup[num] = list(i)
    num += i

for i in student_tup :
    i.append(float(input("{}학생의 학점 : ".format(i[0]))))
    sum += i
'''
for i in dict1.values() :
    i.append(float(input("{}학생의 학점 : ".format(i[0]))))
    sum += i[2]
print("=== 학생 정보 목록 ===")
for key, value in dict1.items() :
    print("{" + "\'{}\' : {}".format(key, value)+"}" )
print("전체 학생의 평균 학점은 {:.1f}점 입니다.".format(sum/len(student_tup)))