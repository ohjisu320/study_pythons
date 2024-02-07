# 문제 설명
# 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1,
#  두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 
# 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(numer1, denom1, numer2, denom2):
    numer3 = numer1*denom2+numer2*denom1
    denom3 = denom1*denom2
    count = numer3/denom3
    while type(count)== int and type(numer3)== int and type(denom3)== int :
        print("int")
        count = numer3/denom3
        numer3=(numer3/count)
        denom3=(denom3/count)
    answer = [numer3, denom3]
    return answer

print(solution(5,6,3,4))