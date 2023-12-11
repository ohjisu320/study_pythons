# class arithmetics에 곱셈, 나눗셈 추가
# 뺄셈 곱셈 나눗셈 실행

class Arithmetics :
    def add(self, first, second): 
        result = first+second
        return print(result)  
    def minus(self, first, second) :
        result = first-second
        return print(result)
    def muliply(self, first, second): 
        result = first*second
        return print(result)  
    def division(self, first, second) :
        result = first/second
        return (result)

arithmetics=Arithmetics()
print(arithmetics.minus(5, 6))
print(arithmetics.muliply(5, 6))
print(arithmetics.division(5, 6))
