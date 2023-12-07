## call by referrence -  묶음처리:재사용가능
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

# list_fruits = ["melon", "apple", "banana", "cherry"]
# list_fruits[0]

def return_list() :
    list_fruits = ["melon", "apple", "banana", "cherry"]
    return list_fruits
print_list=return_list()
print("return_list() return result : {}".format(print_list))

list_fruits = ["melon", "apple", "banana", "cherry"]
list_fruits[0]

#list 중에서 index로 값 return
def return_listbyindex():
    list_fruits = ["melon", "apple", "banana", "cherry"]
    return list_fruits[0]
print("return fuction return_listbyindex() : {}".format(return_listbyindex()))


# my_score = 79

# if my_score >= 90 : # 90점 이상: A
#     print("{}점은 90점 이상으로 A 학점.".format(my_score))
# elif my_score > 80 : # 80점 초과: B
#     print("{}점은 80점 초과이므로 B 학점.".format(my_score))
# else :               # 나머지 F
#     print("{}점은 80점 이하이므로 F 학점.".format(my_score))
# print("End Program!")

# print 작업 반복을 줄이는 function 만들기
def return_grade() :
    my_score = 79
    my_grade = ''
    if my_score >= 90 : # 90점 이상: A
        my_grade='A'
    elif my_score > 80 : # 80점 초과: B
        my_grade='B'
    else :               # 나머지 F
        my_grade='F'
    return my_grade
str_grade=return_grade()
print("당신의 학점 : {}.".format(str_grade))

def return_grade() :
    my_score = 79
    if my_score >= 90 : # 90점 이상: A
        my_grade='A'
    elif my_score > 80 : # 80점 초과: B
        my_grade='B'
    else :               # 나머지 F
        my_grade='F'
    return my_grade
    #function을 만들어 두면 다른 function 안에서도 호출(call)할 수 있음.
    return_listbyindex()
str_grade=return_grade()
print("당신의 학점 : {}.".format(str_grade))