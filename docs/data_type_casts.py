pass
type("jisuoh") #문자 type
# <class 'str'>
type(2000) #숫자 type
# <class 'int'>

name = "jisuoh!" #문자 type
type(name)
# <class 'str'>

age=24 #숫자 type
type(age)
# <class 'int'>

#터미널 입력 값에 대한 확인 - terminal에서 들어온 data의 data type은 일괄적으로 string으로 인식
str_input=input("문자 입력 : ")
print("입력({}) type 표시 : {}".format(str_input, type(str_input)))
num_input = input("숫자 입력 : ")
print("입력({}) type 표시 : {}".format(num_input, type(num_input)))
# cast - data type 변경
int(num_input)
# 2010
type(int(num_input))
# <class 'int'>

# cast 불가 경우 - 문자를 숫자로 바꿀 때
pass
mix_val = "23k"
int(mix_val)
# Traceback (most recent call last):
#  File "<string>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '23k'