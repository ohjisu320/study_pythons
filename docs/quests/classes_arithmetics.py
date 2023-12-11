# class arithmetics에 곱셈, 나눗셈 추가
# 뺄셈 곱셈 나눗셈 실행

class Arithmetics :
    def __init__(self) : # 생성자(class가 갖고 있는 자원(function))
        pass

    def add(self, first, second): # 호출 시 변수에 값이 할당됨
        result = first+second
        return print(result)  
    def minus(self, first, second) :
        result = first-second
        return print(result)
    def muliply(self, first, second): # 호출 시 변수에 값이 할당됨
        result = first*second
        return print(result)  
    def division(self, first, second) :
        result = first/second
        return print(result)

arithmetics=Arithmetics()
arithmetics.minus(5, 6)
arithmetics.muliply(5, 6)
arithmetics.division(5, 6)
