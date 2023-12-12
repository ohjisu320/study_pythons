# list 안에 dictionary 구성
dict_car_info_mustang = {
    "brand": "Ford",  
    "model": "Mustang",
    "year": 1964,
    "price" : 30000
}
dict_car_info_sonata = {
    "brand": "Hyundai",
    "model": "Sonata",
    "year": 2020,
    "color": "Black",
    "price": 30000
}

list_car_info = [
    {
    "brand": "Ford",  
    "model": "Mustang",
    "year": 1964,
    "price" : 30000
    },
    {
    "brand": "Hyundai",
    "model": "Sonata",
    "year": 2020,
    "color": "Black",
    "price": 30000
    }

]

list_car_info_k5= {
        "brand": "Kia",
        "model": "K5",
        "color": "White",
        "price": 28000
    }
pass
list_car_info.append(list_car_info_k5)

# "model": "Mustang" 접근 방법 
## 풀이과정 - (list_car_info > index 0번 > dictionary에서 key 호출)
dict_car_info_index_first=list_car_info[0]
dict_car_info_index_first["model"]
pass
## 결과
list_car_info[0]["model"]

#for로 각 dict 정보 출력
for dict_car_info in list_car_info :
    brand=dict_car_info['brand']
    model=dict_car_info['model']
    print("브랜드 : {}, 모델 : {}".format(brand, model))
    pass

pass