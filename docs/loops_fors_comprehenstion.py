# 압축된 for문
numerics = [0, 1, 2, 3 ,4] # 5개수 값으로 이루어진 리스트
numerics_list = [] # numerics + 2 ==> [2, 3 ,4, 5, 6]
for number in numerics :
    result = number + 2
    numerics_list.append(result)
    pass
print(numerics_list)

print([number+2 for number in numerics])
pass
