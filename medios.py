def get_middle_numbers(s, n):

    y = str(n)


    length = s
    if(length % 2 != 0):
        y = "0" + y
    trimmer = len(y) - length
    trimLeft = trimmer/2
    trimRigth = len(y) - (trimmer/2)
         
    r = int(y[int(trimLeft):int(trimRigth)])


    return r