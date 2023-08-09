# 02_A+B
# Baekjoon_1000
# 작성자 : 이지현

result = 0
s = input()
l = s.split(' ')
for i in l:
    result += int(i)
print(result)


# split 함수 
'''
문자열을 잘라 배열로 변환
문자열.split()

문자열.split('구분자')

문자열.split('구분자', 분할횟수)

문자열.split(sep='구분자', maxsplit=분할횟수)'''
