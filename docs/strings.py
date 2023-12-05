# #1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?
# #A. Windows B. macOS C. Linux D. Chrome OS E. 기타
# #2. 주로 사용하는 프로그래밍 언어는 무엇인가요?
# #A. Python B. Java C. JavaScript D. C++ E. 기타

# #단순출력
# print("1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?")
# print("A. Windows B. macOS C. Linux D. Chrome OS E. 기타")
# print("2. 주로 사용하는 프로그래밍 언어는 무엇인가요?")
# print("A. Python B. Java C. JavaScript D. C++ E. 기타")

# #단순출력 with 변수
# str_first = "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
# print(str_first)
# str_second = "A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
# print(str_second)
# str_third = "2. 주로 사용하는 프로그래밍 언어는 무엇인가요?"
# print(str_third)
# str_fourth = "A. Python B. Java C. JavaScript D. C++ E. 기타"
# print(str_fourth)

# print("--------------------------------------------------------------------------")

# #두 개의 변수 한번에 출력하기 _ 다른 방식의 print
# #"{}"==변수 하나와 매칭
# print("{} -> {}".format(str_third, str_fourth))

# print("--------------------------------------------------------------------------")

# #두 번 이상 쓰는 경우에는 변수, 한 번만 쓸 것이면 상수를 사용함.
# #하나의 변수 사용 출력
# str_anyone = "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
# print(str_anyone)
# str_anyone = "A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
# print(str_anyone)
# str_anyone = "2. 주로 사용하는 프로그래밍 언어는 무엇인가요?"
# print(str_anyone)
# str_anyone = "A. Python B. Java C. JavaScript D. C++ E. 기타"
# print(str_anyone)

# # 3. 개발자에게 인기 있는 프로그래밍 언어는 무엇인가요?
# # A. Python B. Java C. JavaScript D. C++ E. 기타
# print("--------------------------------------------------------------------------")
# #두개 이상의 변수 사용 출력
# #변수는 [소문자, _]만 사용
# str_question = "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
# print(str_question)
# str_answer = "A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
# print(str_answer)
# str_question = "2. 주로 사용하는 프로그래밍 언어는 무엇인가요?"
# print(str_question)
# str_answer = "A. Python B. Java C. JavaScript D. C++ E. 기타"
# print(str_answer)
# str_question = "3. 개발자에게 인기 있는 프로그래밍 언어는 무엇인가요?"
# print(str_question)
# print(str_answer)

# 다른 방식의 출력 "{}"

# 다중 변수 정의와 값 넣기
multi_val = 3, 5
multi_val
# (3, 5)
num_first, num_second = 3, 5
num_first
# 3
num_second
# 5
"3 5".split()
# ['3', '5']
"6 8".split()
# ['6', '8']

# string split()
first, second = "6 8".split()
first
# '6'
second
# '8'
num_first, num_second = int(first), int(second)

pass






