# 기본 function 형식 - :을 통해 불릴 때만 기능함
def function_name(): #내가 관리할 코드들의 묶음
    pass    # 내용 넣기
    return 0

  
## 형식 연습
def my_function():
  print("Hello from a function")

# function 부르기 - 정의되어 있는대로 부름
my_function()
pass

str_anyone = "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
print(str_anyone)
str_anyone = "A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
print(str_anyone)

# 문항 1과 답항을 출력하는 function 
def print_question_and_answer() : 
    str_anyone = "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
    print(str_anyone)
    str_anyone = "A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
    print(str_anyone)
    return 0
# 반복작업-재활용할 때 좋음.
print_question_and_answer()
print_question_and_answer()
