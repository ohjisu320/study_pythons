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