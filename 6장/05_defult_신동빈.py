'''
    작성일 : 2023년 10일 11일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : 함수의 디폴트 인자.
'''

def order(num,pickle,onion):
    print(f'햄버거{num}개 - 피클 {pickle}, 양파 {onion}')
    
#order(1)    # 오류 발생. - 인자는 1개인데 매개 변수는 3개임.

# 인자가 부족한 경우 기본 값을 넣어 주는 것을 => 디폴트 인자.
def order2(num,pickle = '기본',onion = '기본'):
    print(f'햄버거{num}개 - 피클 {pickle}, 양파 {onion}')

order2(2)
order2(1,pickle = '뻄', onion = '기본')