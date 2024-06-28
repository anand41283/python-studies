#create a function pos_neg with one parameter to find given number is +ve,-ve,or zero
# def pos_neg(n1):
#     if n1==0:
#         return("zero")
#     else:
#         return("+ve" if n1>0 else "-ve")
# print(pos_neg(0))

def pos_neg(n1):
    return "+ve" if n1>0 else "-ve" if n1<0 else "zero"       
print(pos_neg(-9))


