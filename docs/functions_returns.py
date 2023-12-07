## call by value -  묶음처리:재사용가능
## 나오는 값 처리
## return 뒤에 있는 '값'만 나온다는 것 유념

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

list_fruits = ["melon", "apple", "banana", "cherry"]
list_fruits[0]

def return_list() :
    list_fruits = ["melon", "apple", "banana", "cherry"]
    return list_fruits
print_list=return_list()
print("return_list() return result : {}".format(print_list))