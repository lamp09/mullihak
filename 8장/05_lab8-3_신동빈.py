'''
    작성일 : 2023년 11일 08일
    작성자 : 202395019 컴퓨터공학부 신동빈
    설명 : LAB 8-3

'''

partyA = set(["Park", "Kim","Lee"])
partyB = set(["Park","Choi"])

print(f"2개의 파티에 모두 참석한 사람은 {partyA.intersection(partyB)}입니다.") # 교집합
print(f"partyA 와 partyB에 참석한 사람들은 {partyA.union(partyB)}입니다.") # 합집합
print(f"1개의 파티에만 참석한 사람은 {partyA.symmetric_difference(partyB)}입니다.") # 대칭차집합
print(f"파티 A에만 참석한 사람은 {partyA.difference(partyB)}입니다.") # 차집합