# function에 들어가는 값'들' - [한가지, 두가지, ... , 묶음 등 다양함 ]
# 입력하는 것도 값(들), return되는 것도 값


# 들어오는 값에 따라서 return의 내용도 변경되어야 범용화 가능. - 4+5=9만 출력하는 것이 아니라 단순 add 기능


def add(first, second): # 호출 시 변수에 값이 할당됨
    sum = first+second
    return sum  # 상수 대신 변수 사용

# 호출할 때 자동으로 변수에 매칭
# 입력 값에 따라 결과값이 달라짐. add의 기능
if __name__ =="__main__" :
    num_sum=add(5, 4)   #  상수 parameters 사용
    print("add(5, 4) return 결과 : {}".format(num_sum))

    third=6
    fourth=10
    num_sum=add(third, fourth) # 변수 parameters 활용   #  function 부르면 값들만 전달됨.
    print("add(6, 10) return 결과 : {}".format(num_sum))

input_fir=int(input())
input_sec=int(input())
num_sum=add(input_fir, input_sec)   #  변수-input parameters 사용
print("add() return 결과 : {}".format(num_sum))


def return_grade(my_score) : # 자신을 불렀을 때 값들이 들어감.
    if my_score >= 90 : # 90점 이상: A
        my_grade='A'
    elif my_score > 80 : # 80점 초과: B
        my_grade='B'
    else :               # 나머지 F
        my_grade='F'
    return my_grade
    #function을 만들어 두면 다른 function 안에서도 호출(call)할 수 있음.
    # return_listbyindex()

if __name__ == "__main__":
    my_score=88
    str_grade = return_grade(my_score)
    print("당신의 점수는 {}점 이므로 {}학점입니다.".format(my_score, str_grade))

    str_grade=return_grade(99)
    print("당신의 학점 : {}.".format(str_grade))