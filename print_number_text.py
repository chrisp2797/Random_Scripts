#prints the text of a number in english
#supports up to 999.999.999.999.999 (or nine hundred ninety nine trillion 999 billion 999 million 999 thousand 999)
def print_number_hundreds(number):
    if(int(number)==0):
        print("Zero")
        return
    number_names=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    number_names_tens=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]#"" are for easier indexing
    number_str=str(number)
    if len(number_str)==3 and number_str[0]!='0':
        print(number_names[int(number_str[0])]+" Hundred",end= " ")
    number_str=number_str[-2:]
    if(number_str=="00"):return
    if number_str[0]=="0" or number_str[0]=="1" or len(number_str)==1:#if number between 1 and 19
        print(number_names[int(number_str)],end=" ")
    else:
        print(number_names_tens[int(number_str[0])],end=" ")
        print(number_names[int(number_str[1])],end=" ")
    
    

def print_number_text(number,previous=False):
    if(str(number)==""):print();return
    if(int(number)==0 and not previous):
        print("Zero")
        return
    number_str=str(number)
    if len(number_str)>30:
        print("This number is too high")
        return
    if(number_str[:3]=="000"):
        print_number_text(number[3:],True)
    else:
        print_number_hundreds(number_str[:3])
        if len(number_str)>27:print("Octillion",end=' ')
        elif len(number_str)>24:print("Septillion",end=' ')
        elif len(number_str)>21:print("Sextillion",end=' ')
        elif len(number_str)>18:print("Quintllion",end=' ')
        elif len(number_str)>15:print("Quadrillion",end=' ')
        elif len(number_str)>12:print("Trillion",end=' ')
        elif len(number_str)>9:print("Bilion",end=' ')
        elif len(number_str)>6:print("Milion",end=' ')
        elif len(number_str)>3:print("Thousand",end=' ')
        print_number_text(number_str[3:],previous=True)
    

    
        
    
if __name__=="__main__":
    print_number_text(123500000000125000368003)
    '''for i in range(50):
        print_number_text(i)'''