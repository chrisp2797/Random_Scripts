#Prints the text of a number in english
#Supports up to 999,999,999,999,999,999,999,999,999,999 
#or Nine Hundred Ninety Nine Octillion Nine Hundred Ninety Nine Septillion Nine Hundred Ninety Nine Sextillion Nine Hundred Ninety Nine Quintllion 
#Nine Hundred Ninety Nine Quadrillion Nine Hundred Ninety Nine Trillion Nine Hundred Ninety Nine Bilion Nine Hundred Ninety Nine Milion Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine

#Function that prints numbers up to 999
def print_number_hundreds(number):
    if(int(number)==0):#
        print("Zero")
        return
    number_names=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    number_names_tens=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]#"" are for easier indexing
    number_str=str(number)
    if len(number_str)==3 and number_str[0]!='0':#if the number given is >=100
        print(number_names[int(number_str[0])]+" Hundred",end= " ")
    number_str=number_str[-2:]#take the last 2 digits
    if(number_str=="00"):return#if 100,200 etc...
    if number_str[0]=="0" or number_str[0]=="1" or len(number_str)==1:#if number between 1 and 19
        print(number_names[int(number_str)],end=" ")
    else:
        print(number_names_tens[int(number_str[0])],end=" ")#twenty thirty etc
        if number_str[1]!='0':print(number_names[int(number_str[1])],end=" ")#not necessery, just so it doesn't add any more whitespaces than needed
    
    
#This function breaks the number into millions billions etc and prints each hundred with the correct suffix 
def print_number_millions(number_str,previous=False):
    if(number_str==""):print();return#To break recursion
    if(int(number_str)==0 and not previous):#if the number given it's just zero, print zero
        print("Zero")
        return
    if len(number_str)>30:#if the number given is too large
        print("This number is too high")
        return
    if(number_str[:3]=="000"):#for example 1,000,012 is read as one million twelve, we dont mention the thousands, so we skip them
        print_number_millions(number_str[3:],True)
    else:
        print_number_hundreds(number_str[:3])#print the hundred
        #with the correct suffix
        if len(number_str)>27:print("Octillion",end=' ')
        elif len(number_str)>24:print("Septillion",end=' ')
        elif len(number_str)>21:print("Sextillion",end=' ')
        elif len(number_str)>18:print("Quintllion",end=' ')
        elif len(number_str)>15:print("Quadrillion",end=' ')
        elif len(number_str)>12:print("Trillion",end=' ')
        elif len(number_str)>9:print("Bilion",end=' ')
        elif len(number_str)>6:print("Milion",end=' ')
        elif len(number_str)>3:print("Thousand",end=' ')
        print_number_millions(number_str[3:],previous=True)#move on
    
def print_number_text(number):#pre-processing function to add zeroes to the begining of the string number
    number_str=str(number)
    number_str=number_str.zfill(30)#30 because one hundred octillion is 30 digits long
    print_number_millions(number_str)
    
        
    
if __name__=="__main__":
    print_number_text(9012500000000125000368003)
    