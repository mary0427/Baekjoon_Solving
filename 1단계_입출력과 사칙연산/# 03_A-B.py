# 03_A-B
# Baekjoon_1001
# 작성자 : 이지현

l = input().split()
r = int(l[0])-int(l[1])
print(r)


# best
'''
a,b = map(int,input().split())
print(a-b)
'''

# map 함수
두 번째 인자로 들어온 반복 가능한 자료형 (리스트나 튜플)을 첫 번째 인자로 들어온 함수에 하나씩 집어넣음.
# 형태
map(함수, 적용할 값들(리스트, 튜플 등))
  
* map 함수의 반환 값은 map객체 이기 때문에 해당 자료형을 list 혹은 tuple로 형 변환시켜주어야 함.

