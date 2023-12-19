import functions_parameters
#  프로그램에는 main은 무조건 있어야 함.
if __name__ =="__main__":
    # import functions in another file
    num_result = functions_parameters.add(4, 5)
    print("result : {0}".format(num_result))
    pass