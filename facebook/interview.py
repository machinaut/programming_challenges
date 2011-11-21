#!/usr/bin/env python
# Alright! I'm ready for this :-)
#
#  Growth team! sounds cool :-D

"""
Given two input strings representing arbitrary large (positive) integers, how to compute the result of their multiplication?

For instance, the result of "12345678987654321" multiplied by "123456789123456789" is "1524157887364730998475842112635269". 
"""

import copy
class Bigint:
    def __init__(self,string):
        """ string is the number to represent """
        self.integer_parts = list()
        self.parse(string)
        
    def parse(self,string):
        """ successively parse out 32-bit sections of the larger integer, and store them in self.integer_parts """
        # Read in each digit from the right (reverse order) and build 32-bit integers,
        # And each time we fill up a 32-bit integer, we add it to the list self.integer_parts
        a = 0 # signed integer with a fixed size
        for character in reversed(string): # for each digit in the string, starting from the least significant
            a = a * 10
            a += int(character) # "9" -> we add 9 to a
            if a > (2**31): # a < 0
                self.integer_parts.append(a)
                a = a / (2**31) # 2**30 test
        self.integer_parts.append(a)
    
    def multiply(self,n):
        """ Multiplies 'self' BigInt by another BigInt, and returns a new BigInt with that value """
        # multiply self.integer_parts with n.integer_parts
        overflow = 0
        list_partials = list()
        m = max(len(self.integer_parts), len(n.integer_parts))
        
        for i in range(len(self.integer_parts)):
            partial = BigInt("")
            overflow = 0
            selfpart = self.integer_parts[i]
            for j in range(len(n.integer_parts)):
                npart = n.integer_parts[j]
                product = (selfpart * npart + overflow) % (2**31)
                overflow = (selfpart * npart + overflow) / (2**31)
                partial.integer_parts[j] = product
            list_partials.append(copy.copy(partial))
        
        result = BigInt('0')
        for partial in list_partials:
            result = result.add(partial)
        
        return result
        
    def add(self,n):
        """ adds two BigInts"""
        m = max(len(self.integer_parts),len(n.integer_parts))
        overflow = 0
        result = BigInt('')
        for i in range(m):
            if len(self.integer_parts) > i:
                selfpart = self.integer_parts[i]
            else:
                selfpart = 0
            if len(n.integer_parts) > i:
                npart = n.integer_parts[i]
            else:
                npart = 0
            product = (selfpart + npart + overflow) % (2**31)
            overflow = (selfpart + npart + overflow) / (2**31)
            result.integer_part[i] = product
        return result
            
            
        
    def toString(self):
        """ print out self in decimal form """
        string = "" # build the output
        overflow = 0
        for intpart in self.integer_parts:
            intpart = intpart + overflow
            for i in range(9): # iterates over the intpart
                c = intpart % 10  # 2**31 == 2147483648, 10 decimal digits
                string = str(c) + string # converts c to a string, just the decimal number, and prepend it to string
                intpart = intpart / 10
            overflow = intpart
        string = str(overvlow) + string
        return string

"""
a = BigInt("12345678987654321")
b = BigInt("123456789123456789")
result = a.multiply(b)
print result.toString()
"""

def multiply(a,b):
    """ take a and multiply it by each digit in b """
    result = "0"
    for digit in b:
        partial = "0" # accumulate partial result
        for i in range(int(digit)): # add a to it 'digit' times
            partial = add(partial,a)
        result = add(result+"0",partial)
    return result
    
def add(a,b):
    # Even out the lengths
    b = [0]*(len(a)-len(b)) + [int(i) for i in b] # pad with zeros, convert to ints
    a = [0]*(len(b)-len(a)) + [int(i) for i in a] # pad with zeros, convert to ints
    s = "" # string to accumulate our answer
    remainder = 0 # hold remainder inbetween loops
    for pair in zip(a,b)[::-1]:
        ac,bc = pair # unpack tuple
        s = str((ac + bc + remainder) % 10) + s # add next digit
        remainder = (ac + bc + remainder) / 10 # save remainder
    if remainder > 0: # if there is another digit remaining
        s = str(remainder) + s
    return s


"""
Given two input strings representing arbitrary large (positive) integers, how to compute the result of their multiplication?

For instance, the result of "12345678987654321" multiplied by "123456789123456789" is "1524157887364730998475842112635269". 
"""
if __name__ == "__main__":
    print "1524157887364730998475842112635269"
    print multiply("12345678987654321","123456789123456789")

