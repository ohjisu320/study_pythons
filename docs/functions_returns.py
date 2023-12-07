## 나오는 값 처리


def add():
    first = 5
    second = 4
    sum = first+second
    return 0

num_sum=add()
print("add() return 결과 : {}".format(num_sum))

# num_sum = add()


def function_add():
    first = 5
    second = 4
    sum = first+second
    return sum  # 상수 대신 변수 사용

num_sum=function_add()
print("add() return 결과 : {}".format(num_sum))

num_first=4
num_second=5
# 곱셈 연산
num_first * num_second

def multiply(): 
    num_first=4
    num_second=5
    # 곱셈 연산
    result=num_first * num_second
    return result
num_multiply = multiply()
print("num_multiply() return value : {}".format(num_multiply))