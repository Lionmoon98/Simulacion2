
def mid_square(n,x0):
    
    d = len(str(x0))
    r = []
       
    for i in range(n):
         y = x0*x0
         x0 = get_middle_numbers(d,y)
         r.append (float("0." + str(x0)))
    return r

def mid_product(n,x0,x1):
    d = len(str(x0))
    r = []
       
    for i in range(n):
         y = x0*x1 
         temp = x1
         x1 = get_middle_numbers(d,y)
         x0 = temp
         r.append (float("0." + str(x1)))
    return r

def constant_multiplier(n,a,x0):
    d = len(str(x0))
    r = []
       
    for i in range(n):
         y = a*x0
         x0 = get_middle_numbers(d,y)
         r.append (float("0." + str(x0)))
    return r

def get_middle_numbers(s0, n0):
    
    y0 = str(n0)

    length = s0
    if(length % 2 != 0):
        y0 = "0" + y0

    Postion = len(y0) - length
    Left = Postion/2
    Rigth = len(y0) - (Postion/2)
         
    r = int(y0[int(Left):int(Rigth)])

    return r

