def home(value) :
    html = "<body> It's Home. value {} </body>".format(value)
    return html

def error() :
    html = "<body> It's Error. value {} </body>".format(value)
    return html


# 항시 응답하는 프로그램
while True : 
    work, value = input('업무 / 해당값 : ').split()
    print("work : {}, value ho: {}".format(work, value))
    if work == "home" :
        result  = home()
        print(result)
    else :
        result  = error()
        print(result)