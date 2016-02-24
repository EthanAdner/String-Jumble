"""He
stringjumble.py
Author: Ethan Adner 
Credit: Payton Stearns

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
x=str(input("Please enter a string of text (the bigger the better): "))
w=list(x)
z=0

#Letters in reverse
while z<len(w):
    y=w[len(w)-z-1]
    print(y,end="")
    z=z+1
print("")
######################
#words in reverse

#splits words apart into letters
z=0
a=""
b=[""]
while z<len(w):    
    
    a=a+str(w[z])
    if w[z]==" ":
        b.append(a)
        a=""
    
    z=z+1
b.append(a+" ")
print(b)
b.remove("")
#print(b)
#print(w)
z=0
#reverses words

while z<len(b):
    y=b[len(b)-z-1]
    print(y,end="")
    z=z+1
print("")

##################

"""
z=0
a=[]
g=""
while z< len(w):
    
    #if z==len(w):
     #   z=z-1
    if str(w[z])==" ":
        #print(a)
        t=0
        while t<len(a):
            y=a[len(a)-t-1]
            print(y,end="")
            t=t+1
        print("",end="")
        a=[]
    a.append(w[z])
    z=z+1
'''ethan likes to eat all the ...'''
   
t=0
while t<len(a):
    y=a[len(a)-t-1]
    print("{0}".format(y),end="")
    t=t+1
print("", end=" ")

#print(a)
"""