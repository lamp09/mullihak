'''
    작성일 : 2023년 11일 15일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 문자열
'''

text = "There's a reason some people are working to make \
    it harder to vote, especially for people of color \
        It's because when we show up, things change."
        
# 띄어쓰기로 문자열로 분리하고, 단어의 개수를 찾아라.
# len() => 길이(개수) : 리스트의 항목 개수 찾는 함수
print(len(text.split()))

# 도전문제 9-1 
# 회사 이름은 *로 표시
# kT, Samsong, LG, SKT 

# 변수 저장
text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG U+ Mystic Pink 30%, SKT Mystic Blue not disclosed) '
com_len = []
com_text = ['skt', 'kt', 'lg', 'samsung']
cLenSort = [[0],[]]
# 소문자 변환
text = text.lower()
# 텍스트에 회사명이 있는지 찾아서 check 변수에 저장
check = [i for i in text.split() if i in com_text]
print(check)

# 회사명 *로 변환
for i in range(0,len(check)):
    j = check[i]
    num = 0
    for k in range(0,len(cLenSort[0])):
        k1 = cLenSort[0][k]
        if k1 <= len(j):
            cLenSort[0].insert(num,len(j))
            cLenSort[1].insert(num,j)
            break
        num += 1

for i in cLenSort[1]:
    text = text.replace(i,'*')
print(text)
    
