# 같은 폴더에ㅓ 있는 class and functions 호출


# 1. import -- 같은 file에 있을 경우, 생략
import classes_formats
# 2. class intance -- class 이름 호출
person = classes_formats.Person()
arithmetics = classes_formats.Arithmetics()
class_name = classes_formats.Class_name()
# 3. call function
person.add_age()

## import 시 주로 사용하는 방식
from classes_formats import Person, Arithmetics, Class_name
person_second=Person()
arithmetics_second = Arithmetics()
pass