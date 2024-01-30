# call back funciton
def add(first, second) :    # 호출 시 변수에 값이 활당됨
    sum = first + second
    # return 0
    return sum  # 상수 대신 변수 사용

def multiply(first, second) :    # 호출 시 변수에 값이 활당됨
    result = first * second
    # return 0
    return result  # 상수 대신 변수 사용


def process_call_function(first, second, callback_fucntion):
    result = callback_fucntion(first,second)
    return result

if __name__ == '__main__' :
    # result = add(5,6)
    result_add = process_call_function(5, 6, add)
    result_multiply = process_call_function(5, 6, multiply)
    pass