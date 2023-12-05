#input() - 기본 사용
#str_start="Start, Programming."
#print ("{}".format(str_start))
#str_input_desc = "영문이름 입력 : "
#str_input=input("{}".format(str_input_desc))
#pass

#input() - 숫자 받아 환산하기
#풀기: 출생년도 입력 받아 나이 계산 (예. 2023(올해) - 2000(출생년도) = 나의 나이)
str_start="Start, Programming."
print ("{}".format(str_start))
num_input_desc = "출생년도 입력 : "
num_input_birthyear=input("{}".format(num_input_desc))
num_age=2023-int(num_input_birthyear)+1
print ("출생년도 기준 내 나이 계산 : {}".format(num_age))
pass