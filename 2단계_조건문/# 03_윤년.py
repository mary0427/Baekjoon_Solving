# 2-3_윤년
# Baekjoon_2753
# 작성자 : 이지현

y=int(input())
if y%4 == 0 :
    if y%100==0 :
        if y%400==0:
            print(1)
        else :
            print(0)
    else :
        print(1)
else:
    print(0)
