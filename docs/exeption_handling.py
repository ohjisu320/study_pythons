# 기본 구문
try :
    pass    # 업무 코드
except :
    pass    # 업무 코드 문제 발생 시 대처 코드(수정하기 위해 쓰일 때도 있음.)
finally :
    pass    # try나 except가 끝난 후 무조건 실행되는 코드
# pure python with 계산기

num_first = '4'
num_second = 5
#  나눗셈 연산



pass

try :
    result=num_first/num_second
    pass    # 업무 코드
except :
    result= int(num_first) / int(num_second)
    pass    # 업무 코드 문제 발생 시 대처 코드(수정하기 위해 쓰일 때도 있음.)
finally :
    pass    # try나 except가 끝난 후 무조건 실행되는 코드

print("{}={}/{}".format(result, num_first, num_second))