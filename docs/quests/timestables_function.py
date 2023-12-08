#source from [study_pythons/docs/quests/timestables_fors.py]

def timestables(x) :
    numbering=[0, 1, 2, 3, 5, 6, 7, 8]
    for loop in numbering:
        print("{}*{}={}".format(x, loop+1,(loop+1)*x))
    return stop()

def stop() :
    str_input=input("구구단 몇단(종료하려면 q 입력) : ")
    if str_input !="q" :
        timestables(int(str_input))
    else :
        print("End Program!")
   
str_input=input("구구단 몇단 : ")
timestables(int(str_input))