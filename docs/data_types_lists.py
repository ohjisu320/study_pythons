# 사용 이유: 값들에 모임을 쉽게 전달
# 숫자 5개 값들로 이루어진 list
list_numerics = [0, 1, 2, 3, 4] 

# 문자 3개 값들로 이루어진 list
list_fruits = ["apple", "banana", "cherry"]

# 숫자 4개와 문자 2개의 값들로 이루어진 list -> 우린 쓰지 않음
list_mix = [0, 1, 2, 3, "apple", "banana"]

len(list_numerics)
#5
len(list_mix)
# 6

#for문 활용 후 다시 오기

# index(색인, 위치값)
list_fruits = ["melon", "apple", "banana", "cherry"]

## index로 값 가져오기
list_fruits [0] # 단일변수로 여김 - 1차원(행)
# 'melon'
list_fruits [3]
# 'cherry'

## error 발생
# list_fruits[4]
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# IndexError: list index out of range    -->   ## index에서 벗어났다는 의미



pass 