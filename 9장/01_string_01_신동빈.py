'''
    작성일 : 2023년 11일 15일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 문자열
'''
# 문자열 슬라이싱
s = 'Happy Day!'
print(s[0])
print(s[6:10])
print(s[:-2]) # 뒤에서 3번째 까지 출력

# 문자열 분리 => spilt()
s = 'Welcome to Python'
print(s.split()) # 공백을 기준으로 분리함

s ='2023.11.15'
print(s.split('.'))

s = 'Hello, World'
print(s.split(','))

s = 'Hello, World'
print(s.split(', '))

# 공백 제거 => strip()
s = 'Welcome, to, Python, and , bla, bla       '
print(s.strip())
print([x.strip() for x in s.split(',')])

print(list('Hello World!'))


# 문자열 연결 => join()
print(','.join(['apple','grape','banana']))     # ,을 붙여서 연결
print('-'.join('010.1234.5678'.split('.')))     # .으로 구분된 번호를 - 로 연결

# . 을 - 로 바꾸기
print('010.1234.2345'.replace('.','-'))

s = 'Hello World!'
print(s)
# 리스트로 문자열 분리 시켜 slist에 저장.
slist = list(s)
print(slist)
# 분리된 문자를 다시 합치기
print(''.join(slist))

# 줄바꿈과 탭이 포함된 문자열 그대로 출력
a_string = 'Today as well, \n\t Happy a Day.'
print(a_string)

# 문자열 자르기
word_list = a_string.split()
print(word_list)

# 다시 합치기
refind_string = " ".join(word_list)
print(refind_string)

# 대소문자 변환과 문자열 삭제
s = 'Hello, World!'
print(s)
print(s.lower()) # 모두 소문자 변환
print(s.upper()) # 모두 대문자 변환

# 공백 제거 strip()
s = '           Hello, World!          '
print(s.strip()) # 양옆 모든 공백 제거
print(s.lstrip()) # 왼쪽 공백 제거 
print(s.rstrip()) # 오른쪽 공백 제거

s = '#######Hello, World!###########'
print(s)
print(s.lstrip('#'))

# 문자열 찾기 
s = 'www.silla.ac.kr'
#.kr 찾기
print(s.find('.kr')) # 12번지 출력
print(s.find('x')) # x가 없기에 -1 출력

# .이 몇 개 인가?
print(s.count('.'))

import wikipedia

wiki = wikipedia.page('Artificial intelligence')

text = wiki.content


from wordcloud import WordCloud

WordCloud = WordCloud(width= 2000, height= 1500).generate(text)

import matplotlib.pyplot as plt

plt.figure(figsize=(40,30))
plt.imshow(WordCloud)
plt.show()