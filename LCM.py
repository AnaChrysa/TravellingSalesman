from math import gcd

def LCM(a, b):
    return a * b // gcd(a, b)

LCMdict={}

def updateLCM(a):
    LCMdict.update({a:{}})
    for x in range(1,a+1):
            LCMdict[a].update({x:LCM(a,x)})
            LCMdict[x].update({a:LCM(a,x)})

for x in range(1,w):#w is the last number done #The code does not understand this variable
  updateLCM(x)
