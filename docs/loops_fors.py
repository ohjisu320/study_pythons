
# 얼마만큼 반복할지에 대한 값'들'을 알려줌
numerics = [0, 1, 2, 3, 4] #5개 값으로 이루어진 list
# 기본 for문
# for 순서있는값 in [variable-list]:
#     pass
# for문은 list와 한 쌍
# for number in numerics :
#     pass
#     print(number)

# 기본 문형
# for x in [] :
#     pass

# 문자 3개 값들로 이루어진 list
# 위치값-index는 0부터 - 0부터 counting됨

for x in ["apple", "banana", "cherry"] : #반복대상 리스트 직접 넣기
    pass
    print("fruit name : {}!".format(x))
print("End Program!")

list_fruits = ["apple", "melon", "banana", "cherry"] 
for str_fruit in list_fruits : #반복대상 리스트 변수로 넣기
    pass
    print("fruit name : {}!".format(str_fruit))
print("End Program!")
pass

numerics = [0, 1, 2, 3 ,4]
for number in numerics :
    pass
    print("Number : {}.".format(number+2))
print("End Program!")

## 설문 답변 받기
# 두개씩 띄어서 출력

list_polls=[ "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
            ,"A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
            ,"2. 주로 사용하는 프로그래밍 언어는 무엇인가요? "
            ,"A. Python B. Java C. JavaScript D. C++ E. 기타"
            ,"3. 개발자에게 인기 있는 프로그래밍 언어는 무엇인가요?"
            ,"A. Python B. Java C. JavaScript D. C++ E. 기타"]


list_statistics = [0, 0, 0, 0, 0] # 답항만큼 0을 넣어줌
for num_count in [0,2,4]:
    # 질문 
    str_questions = list_polls [num_count]
    print("{}".format(str_questions))
    # 답변 항목
    str_answer = list_polls [num_count+1]
    print("{}".format(str_answer))
    # 답변 입력
    str_questions_result=input("당신의 답변(A~E를 순서에 맞게 번호로 입력) : ")
    num_questions_result=int(str_questions_result)
    index = num_questions_result - 1 # index 위치값
    list_statistics[index]=list_statistics[index]+1
    
    print("------------------------------------------")
    pass
print("선호답항: {}".format(list_statistics))
print("End Program!")
