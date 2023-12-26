# 코드 기본 형식

# import 시 주로 사용하는 방식
from classes_formats import Person, Arithmetics, Class_name
# class basic format
class Class_name :
    def __init__(self) : # 생성자
        pass
    def function_name(self) :  # self 키워드 필요(class 소속 확인용)
        try :
            pass    # 업무 코드
        except :
            pass    # 업무 코드 문제 발생 시 대처 코드(수정하기 위해 쓰일 때도 있음.)
        finally :
            pass    # try나 except가 끝난 후 무조건 실행되는 코드    
        return 0

# 기본 function 형식 - :을 통해 불릴 때만 기능함
def function_name(): 
    try :
        pass    # 업무 코드
    except :
        pass    # 업무 코드 문제 발생 시 대처 코드(수정하기 위해 쓰일 때도 있음.)
    finally :
        pass    # try나 except가 끝난 후 무조건 실행되는 코드    
    return 0

if __name__=="__main__":
    # 기본 구문
    try :
        pass    # 업무 코드
    except :
        pass    # 업무 코드 문제 발생 시 대처 코드(수정하기 위해 쓰일 때도 있음.)
    finally :
        pass    # try나 except가 끝난D 후 무조건 실행되는 코드

