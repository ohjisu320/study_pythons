# class arithmetics에 곱셈, 나눗셈 추가
# 뺄셈 곱셈 나눗셈 실행

class Arithmetics :
    def add(self, first, second): 
        result = first+second
        return result 
    def minus(self, first, second) :
        result = first-second
        return result
    def multiply(self, first, second): 
        result = first*second
        return result  
    def division(self, first, second) :
        result = first/second
        return result

arithmetics=Arithmetics()
first=int(input("first : "))
second=int(input("second : "))

print("{}-{}={}".format(first, second, arithmetics.minus(first, second)))
print("{}*{}={}".format(first, second, arithmetics.multiply(first, second)))
print("{}/{}={}".format(first, second, arithmetics.division(first, second)))
