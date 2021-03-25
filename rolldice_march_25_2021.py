"""Program to roll dice (qty 2) each time <enter> is pushed.
Intended to be a Python programming learning experience for me and my grandson.
"""

import random
min = 1
max = 6
c = int()
d = int()
e = int()
f = int()
g = int()
h = int()
p = int()
tt = int()
cc = int()
dd = int()
ee = int()
ff = int()
gg = int()
hh = int()


for i in range(25):  #roll dice 25 times

    input("press <enter>")
    
    print ("Rolling the dice...")
    print ("The values are....")
    a=(random.randint(min, max))
    b=(random.randint(min, max))
    print ("First Die", a)
    print ("Second Die",b)
    if (a == 1):
        c=c+1
    if (b==1):
        c=c+1    
    if (a == 2):
        d=d+1
    if (b==2):
        d=d+1    
    if (a == 3):
        e=e+1
    if (b == 3):
        e=e+1     
    if (a == 4):
        f=f+1
    if (b==4):
        f=f+1    
    if (a == 5):
        g=g+1
    if (b==5):
        g=g+1     
    if (a == 6):
        h=h+1
    if (b == 6):
        h=h+1    
    if ((a==1)and(b==1)):
        cc=cc+1
    if ((a == 2)and(b==2)):
        dd=dd+1
    if ((a == 3)and(b==3)):
        ee=ee+1
    if ((a == 4)and(b==4)):
        ff=ff+1
    if ((a == 5)and(b==5)):
        gg=gg+1
    if ((a == 6)and(b==6)):
        hh=hh+1
    if (a==b):
        print ("You rolled a pair! This was your pair #",p+1)
        p=p+1
    tt = c+d+e+f+g+h  
    
    print ("Number of total dice rolled", tt, " and the # of rolls", int(tt/2))
    print ("Quantity of rolled <1> is: ",c, "or ", round(c/tt*100,2), "%")
    print ("Quantity of rolled <2> is: ",d, "or ", round(d/tt*100,2), "%")
    print ("Quantity of rolled <3> is: ",e, "or ", round(e/tt*100,2), "%")
    print ("Quantity of rolled <4> is: ",f, "or ", round(f/tt*100,2), "%")
    print ("Quantity of rolled <5> is: ",g, "or ", round(g/tt*100,2), "%")
    print ("Quantity of rolled <6> is: ",h, "or ", round(h/tt*100,2), "%")
    print ("Quantity of pairs =",p)
    print ("Qty of pairs, 1,2,3, etc. are:",cc,dd,ee,ff,gg,hh)
    print ("Pair of 1's: ",cc, "    Pair of 2's: ",dd, "    Pair of 3's: ",ee)
    print ("Pair of 4's: ",ff, "    Pair of 5's: ",gg, "    Pair of 6's: ",hh)
    print(" ")
    print(" ")