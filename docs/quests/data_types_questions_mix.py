
def questions_form() :
    dict_questions = {}
    dict_questions["question"]=input("quest : ")
    dict_questions["answer"]=[]
    for answer_loop in range(4) :
        dict_questions["answer"].append(input("answer : "))
    dict_questions["correct_index"]=input("correct_index : ")
    dict_questions["score"]=input("score : ")
    return dict_questions

def question_loop(loop_num):
    list_question= []
    for i in range(loop_num) :
       list_question.append(questions_form())
    return list_question


print(question_loop(3))

