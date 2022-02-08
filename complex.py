'''
Hi Andrew!
Here is my half-ish-finished code for finding the nth root of any complex number.

****
The functions for certain numbers for n are unfinished...however what does work is:
Quartic root for any complex number
Square root for any complex number
(Everything is else in still a work in progress!)
****

The code is...well...not finished. I am having trouble writing out a function/formula
for a^3 ± b^3 and, of course, other prime numbers for the nth root as well (like finding
the 5, 7, or 11th root of any complex number). I'm not exactly sure how to write a math
program that can use an actual variable 'x' within the euqation. All I know how to do is,
when I'm writing out the formula, to rearrange the equation to have the unknown variable
'x' alone on one side of the equal sign. However, I realize that in order to find
a^3 ± b^3 (in this case, what I'm trying to solve looks more like:
                    0 = x^3 - (sqrt(5+7i))
without using built in calculator function (which I can't find anyways)
or a^5 ± b^5, I need to use this unknown variable 'x'. Right now, I'm not sure how to
do that without breaking the code since, after all, you can't just plug numbers into
0 = x^3 - (sqrt(a+bi)).

...or can you?!!!!

Since I know you are a math-coding-whiz, please let me know if you have any suggestions
or ideas on how to approach this. Maybe I need to program it like an actual calculator
and have it graph it??? Or, if there is a formula out there already, I would greatly
appreciate a hint! I know there is a TON of debugging and more work to do, as well as
explaining all of my confusing comments! Tutorial may be a good time
to go through all of this with you.


Thank you so much for allowing me to pursue this as my "cubic/quartic" root project!
I feel that, with conditionals in programming, it is easier to explain my steps and
thinking!

Best,
Charlotte

'''



import math
import cmath


#still a complex number so function name is a little deceiving, sorry
def nthRealRoots(num,root):
    answer = num**(1/root)             #for the first root of ±
    answer2 = -1 * answer              #for the second root of ±
    return answer, answer2


#complex number that is, IN ADDITION, multiplied by j (double complex) :)
def nthImagRoots(num,root):
    answer = num**(1/root)
    answer2 = -1 * answer
    
    #ANSWER1: for the real component that is going to become the imag component
    imag = str(round(answer.real, 2)) + 'j' #the real component actually becomes the imag
               
               
    #ANSWER1: for the imag component that is going to become the real component
    imagi = str(round(answer.imag,2))
    real = imagi[:(len(str(imagi)))] #taking out the j since j^2 just makes -1
    
    
    #ANSWER1: creating the answer string
    if imag[:1] == '-':     #when imaginary term is negative
        answer = real + ' - ' + imag[1:]
    else: #when imaginary term is positive
        answer = real + ' + ' + imag

    
    #-------
    
    #ANSWER2: for the real component that is going to become the imag component
    imag2 = str(round(answer2.real, 2)) + 'j' # real component actually becomes the imag

    
    #ANSWER2: for the imag component that is going to become the real component
    imagi2 = str(round(answer2.imag,2))
    real2 = imagi2[:(len(str(imagi2)))] #taking out the j since j^2 just makes -1
    
    
    #ANSWER2: creating the answer string
    if imag2[:1] == '-':     #when imaginary term is negative
        answer2 = real2 + ' - ' + imag2[1:]
    else: #when imaginary term is positive
        answer2 = real2 + ' + ' + imag2
    
    return answer, answer2



 
 
#seeing how many 2's and 3's factors are in n --> whether to do diff of sq or a^3 ± b^3
def primeFactors(n):
   # no of even divisibility
   factors = {}
   amountOfTwos = 0
   while n % 2 == 0:
      amountOfTwos += 1
      factors[2] = amountOfTwos
      n = n / 2
   # n reduces to become odd
   for i in range(3,int(math.sqrt(n))+1,2):
      # while i divides n
      iAMOUNT = 0
      while n % i== 0:
         iAMOUNT += 1
         factors[i] = iAMOUNT
         n = n / i
   # if n is a prime
   if n > 2:
         factors[n] = 1
   return factors #returns dictionary of the amount of 2's and 3's in n


def justACalculator(num, root):
    answer = num**(1/root)
    return answer
    
    
    
    
#-----------------

allTheRoots = []

print()
print('the nth root of any complex number')

starterQ = input('Does your complex number contain an imaginary component? (y/n) ')

#if the user chooses to input a complex number that has an imaginary component
if starterQ.lower() == 'y':
    print()
    print('a+bi is your complex number...')
    print()
    a = input('Enter your value for \'a\':  ')
    b = input('Enter your value for \'b\':  ')
    n = input('Enter the number of roots:  ')
    complexNum = complex(int(a),int(b))
    
    
    n = int(n)
    dict = primeFactors(n)
    
    if n % 2 == 0:     #if n is even
        
        if (n > 2): #if n is greater than 2...since n is either 2 or something greater than 2
        
            for cycle in range(int(dict[2]/2)): #for the amount of 2-prime-factors of n
                
                #STILL NOT DONE, NEED TO CHANGE THE CODE TO EMBED SQRT WITHIN SQRT
                #(for 8th root and such)
                #right now only works for quartic root
                #trying to do 6th roots now as well
                #(since it requires doing a^3 ± b^3 formula)
                
                #-----For the real roots------
                x1, x2 = nthRealRoots(complexNum, n)
                
                #for the first root of ±
                real1 = round(x1.real,2)
                imag1 = round(x1.imag,2)
                imagi1 = str(imag1)
                
                if imagi1[:1] == '-':     #when imaginary term is negative
                    theNum1 = str(real1) + ' - ' + str(imagi1[1:]) + 'j'
                    allTheRoots.append(theNum1)
                else: #when imaginary term is positive
                    theNum1 = str(real1) + ' + ' + str(imag1) + 'j'
                    allTheRoots.append(theNum1)
                   
                   
                #for the second root of ±
                real2 = round(x2.real,2)
                imag2 = round(x2.imag,2)
                
                imagi2 = str(imag2)
                
                if imagi2[:1] == '-':     #when imaginary term is negative
                    theNum2 = str(real2) + ' - ' + str(imagi2[1:]) + 'j'
                    allTheRoots.append(theNum2)
                else: #when imaginary term is positive
                    theNum2 = str(real2) + ' + ' + str(imag2) + 'j'
                    allTheRoots.append(theNum2)
                    
                
                #-----For the imag roots------
                y1, y2 = nthImagRoots(complexNum, n)
                allTheRoots.append(y1)
                allTheRoots.append(y2)
            
                
        elif n == 2: #if n IS 2...since n is either 2 or something greater than 2
        
            x1, x2 = nthRealRoots(complexNum, n)
            
            #for the first root of ±
            real1 = round(x1.real,2)
            imag1 = round(x1.imag,2)
            imagi1 = str(imag1)
            
            if imagi1[:1] == '-':     #when imaginary term is negative
                theNum1 = str(real1) + ' - ' + str(imagi1[1:]) + 'j'
                allTheRoots.append(theNum1)
            else: #when imaginary term is positive
                theNum1 = str(real1) + ' + ' + str(imag1) + 'j'
                allTheRoots.append(theNum1)
               
               
            #for the second root of ±
            real2 = round(x2.real,2)
            imag2 = round(x2.imag,2)
            
            imagi2 = str(imag2)
            
            if imagi2[:1] == '-':     #when imaginary term is negative
                theNum2 = str(real2) + ' - ' + str(imagi2[1:]) + 'j'
                allTheRoots.append(theNum2)
            else: #when imaginary term is positive
                theNum2 = str(real2) + ' + ' + str(imag2) + 'j'
                allTheRoots.append(theNum2)
        
        
        else: # if someone tried to find the one-root?? idk
            print('This calculator doesn\'t do that type of math. Sorry!')
                
                
        three = 3
        if three in dict.keys(): #if n (which is even) is ALSO divisible by 3
            for cycle in range(dict[3]):
                
                #add code on doing the a^3-b^3 formula
                # add quadratic formula function at top of page as well
                #appendit to list
                print('testing for life here')
        
        
    elif n % 2 != 0: #if n is odd
        three = 3
        if three in dict.keys():
            for cycle in range(dict[3]): #the cycles of doing the a^3-b^3 formula
                #do the a^3-b^3 formula here
                
                #append it to list
                print('testing for 7')
                
                if cycle != dict[3] - 1: #prepping for next "3" cycle
                    n = n/3
           
        
            #add code on doing the a^3-b^3 formula
            # add quadratic formula function at top of page as well
        
        
        
        else: #the weird prime roots like 5, 7 etc
            print('testing for something')
            #for the other primes beside 2 and 3
            
    
        



            
            
            
        
           
#if the user chooses to input a real number
elif starterQ.lower() == 'n':
    print()
    print('a is your real number, and n is the number of roots...')
    print()
    a = input('Enter your value for \'a\':  ')
    n = input('Enter your value for \'n\':  ')
    complexNum = int(a)
    n = int(n)
    
    
    x1, x2 = nthRealRoots(complexNum, n)
                
    #for the first root of ±
    real1 = round(x1.real,2)
    imag1 = round(x1.imag,2)
    imagi1 = str(imag1)
    
    
    if str(imagi1[:4]) == '0.0': #if imag component is just 0
        theNum1 = str(real1)
        
    else:
        if imagi1[:1] == '-':     #when imaginary term is negative
            imagi1 = imagi1[1:]
            theNum1 = str(real1) + ' - ' + str(imagi1) + 'j'
        else: #when imaginary term is positive
            theNum2 = str(real1) + ' + ' + str(imag1) + 'j'
    
    allTheRoots.append(theNum1)
    
    
       
       
    #for the second root of ±
    real2 = round(x2.real,2)
    imag2 = round(x2.imag,2)
    imagi2 = str(imag2)
    
    #formatting stuff
    if str(imagi2[:4]) == '0.0': #if imag component is just 0
        theNum2 = str(real2)
        
    else:
        if imagi2[:1] == '-':     #when imaginary term is negative
            imagi2 = imagi2[1:]
            theNum2 = str(real2) + ' - ' + str(imagi2) + 'j'
        else: #when imaginary term is positive
            theNum2 = str(real2) + ' + ' + str(imag2) + 'j'
    
    allTheRoots.append(theNum2)
        
    
    #-----For the imag roots------
    y1, y2 = nthImagRoots(complexNum, n)
    allTheRoots.append(y1)
    allTheRoots.append(y2)
    
    
  


for element in allTheRoots: #printing all the roots!
    print(element)
