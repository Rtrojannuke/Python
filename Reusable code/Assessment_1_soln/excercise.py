"""
A function which accepts arguments of State and grossincome, then calculates the tax as per state
It then proceeds to calculting net income by subtracting tax from grossincome
"""
#definning the function
def taxremover(state, income):
    #Available states in the codes
    stt = {"ALA":10,"DRR": 9}
    tax = income - (income*.10);
    for key in stt:
        if state in stt.keys():
            print("YOUR STATE TAX IS: ",stt[state])
            nb = stt["%s"%state]
            tax = tax - ((nb/100) * income)
        else:
            return 1 #Code stops running at this point and break out from the code
    net = income - tax
    print("YOUR STATE IS %s AND NET SALARY IS: %.2f"%(state,net))

taxremover("ALA",1000)
taxremover("DRR",1000)
