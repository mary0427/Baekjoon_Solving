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
문자열을 잘라 리스트로 변환하는 함수.

# 형태 
string.split(seperator, maxsplit)
Separator : 구분 기호. 구분 기호를 사용하여 split 함수는 기본 문자열을 여러 하위 문자열로 분할합니다.
Maxsplit 매개변수: 분활횟수. 문자열 기준을 최대 발생 횟수로 분할하기 위해 함수에 전달되는 숫자입니다.
반환: split 함수는 기본 문자열을 나누거나 분할한 후 문자열 목록으로 돌아갑니다.
