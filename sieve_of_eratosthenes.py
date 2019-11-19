#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 

#import numpy as np
import math

def sieve(n):
    nList = list(range(2,n+1))
    for i in range(2,(math.ceil(n**0.5))+1):
        if nList[i-2] == 0: # check if its a multiple
            continue # if so, move to next number
        for j in range(i-1,n-1):
            if nList[j] == 0:
                continue
            if not nList[j]%i:
                nList[j] = 0
    for m in nList:
        if m != 0:
            print(m)

    
if __name__ == '__main__':
    sieve(100)