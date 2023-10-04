'''
    작성일 : 2023년 10일 04일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 반복을 제어하는 break, continue
    교재 137 페이지
    test word : programing
    
'''

word = input('단어를 입력하세요 : ')

print('===break1===')
for i in word :
    if i =='a' or i =='e' or i =='i' or i == 'o' or i == 'u' : # i 에  a,e,i,o,u 가 있다면 출력 중단
        break
    else : 
        print(i,end='') # 결과 예상 : pr
        
print()

print('=== break2 ===')
for i in word :
    if i in ['a','e','o','i','u','A','E','I','O','U']: # i 에  a,e,i,o,u 가 있다면 출력 중단
        break  # 반복을 중단한다.  반복을 빠져 나간다.
    else : 
        print(i,end='')
        
print()

print('=== continue1 ===')
for i in word :
    if i in ['a','e','o','i','u','A','E','I','O','U']:
        continue # 반복의 처음으로 돌아간다. 아래 문장을 만날 수 없다.
    else : 
        print(i,end='') # 결과 예상 : prgrmng