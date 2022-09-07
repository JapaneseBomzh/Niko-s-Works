import time     
from math import *
while True:
    try:
        print("Select a task(1-3): ")
        Ch=int(input())
        if  1<=Ch <=3  :
            break
        else:
           print("Error")
        continue 
    except ValueError:
        print("error")
        continue
while True:
  try:  
    if Ch == 1:
        print("Determine which equality is more accurate:18^0.5=4.24 or 17/11=1.545")
        time.sleep(1)
        print("Variant 15")
        time.sleep(1)
        x1=sqrt(18)
        x1_1=4.24
        y1=17/11
        y1_1=1.545
        if abs((x1 - x1_1)/x1) > abs((y1 - y1_1)/y1):
            print("Equality 2 is more accurate")
        elif abs((x1 - x1_1)/x1) == abs((y1 - y1_1)/y1):
            print("Equalities are equally exact")
        else:
            print("Equality 1 is more accurate")
    if Ch ==2:
        print("Determine the number of correct significant digits of an approximate number: a) the number 0.8647+-0.0013 in the narrow sense; b) number 24.3618; δ=0.0022 in the broad sense;")
        time.sleep(1)
        print("Variant 15")
        time.sleep(1)
        x_a=0.8647
        y_a=0.0013
        x_b=24.3618
        y_b=0.0022
        n=1
        m=1
        print("A) 8*10^(-1)+6*10^(-2)+4*10^(-3)+7*10^(-4)")
        while y_a<=0.5*10**(1-n+1):
            n+=1
            continue
        print("n=",n-1,"\n")
        time.sleep(1)
        print("B) 2*10^1+4*10^0+3*10^(-1)+6*10^(-2)+1*10^(-3)+8*10^(-4)")
        while x_b*y_b<=1*10**(0-m+1):
            m+=1
            continue
        print("n=",m-1,"\n")
    if Ch ==3:
        print("Find the marginal absolute and relative errors of numbers: а) 2.4516; b) б) 0.863, if they have only correct numbers: a) in the narrow sense; b) in a broad sense.")
        time.sleep(1)
        print("Variant 15")
        time.sleep(1)
        def Dignificant_digits(n):
            u=0
            if str(float(n))==n:
                if float(n)<1:  # якщо вписати 0.0... або 0.100...- рахує лишні нулі в значущі цифри (Баг)
                    u+=2
                else:
                    u+=1
            if float(n)<0:
                u+=1
            return len(n)-u
        #3a
        n_a=Dignificant_digits('2.4516')
        𝛥𝑥=0.5*10**(1-n_a+1)
        𝛿𝑥=abs(𝛥𝑥/2.4516)
        print("𝛥𝑥= ",𝛥𝑥,",","𝛿𝑥= ",𝛿𝑥,"(",(𝛿𝑥*100),"% )") 
        #3b
        n_b=Dignificant_digits('0.863') 
        𝛥𝑥=1*10**(0-n_b+1)
        𝛿𝑥=abs(𝛥𝑥/0.863)
        print("𝛥𝑥= ",𝛥𝑥,",","𝛿𝑥= ",𝛿𝑥,"(",(𝛿𝑥*100),"% )") 
    break
  except ValueError:
   print("error")
   continue


    
