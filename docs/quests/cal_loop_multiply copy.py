# 곱셈 계산기
def multiply(num_first, num_second): # 입력하는 값
    multiply_result=num_first*num_second
    return multiply_result # 나오는 값
def q_sign_result():
    q_program ="End Program!"
    return q_program

cal_number=(input("multiply-first multiply-second : ")).split()
# 곱셈 값 출력
cal_multiply = multiply(int(cal_number[0]), int(cal_number[1]))
print_multiply_result=print("multiply result : {}".format(cal_multiply))
# 종료될 때 까지 반복

# while True :
#     if q_sign_input!="q" :
#         # 곱셈 값 입력
#         cal_number=int(input("multifly first : ")), int(input("multifly second : "))
#         # 곱셈 값 출력
#         cal_multiply = multiply(cal_number[0], cal_number[1])
#         print_multiply_result=print("multiply result : {}".format(cal_multiply))
#     else :
#         break




