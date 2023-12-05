weight, height=input("몸무게(kg) 키(cm) : ").split()
weight=int(weight)
height=int(height)
bmi=weight/(height/100)**2

if bmi >= 25 :
    pass
    print("bmi({})가 25 이상이므로 비만".format(bmi))
elif 23 <= bmi <=24 :
    pass
    print("bmi({})가 23이상, 24 이하이므로 과체중".format(bmi))
elif 18 <= bmi <=22 :
    pass
    print("bmi({})가 18이상, 22이하 이므로 정상".format(bmi))
else :
    pass

    print("bmi({})가 18미만 이므로 저체중".format(bmi))
print("End Program!")