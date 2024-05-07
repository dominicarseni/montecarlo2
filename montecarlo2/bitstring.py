import numpy as np
import math             


class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        '''
        initalizes N, the length of the bitstring. .congig returns an array of zeroes that is the length of the bitstring.
        '''
        self.N = N
        self.config = np.zeros(N, dtype=int)
    
    def __str__(self):
        '''
        returns string that represents object
        '''
        return str(self.config)
    
    def __repr__(self):
        '''
        representation method
        '''
        pass

    def __eq__(self, other):    
        '''
        checks equality of two arrays representing bitstrings, one of which is your original bitstring.
        '''    
        return (self.config==other.config).all()
    
    def __len__(self):
        '''
        returns length of bitstring
        '''
        return len(self.config)

    def on(self):
        '''
        returns number of 1 bits
        '''
        num=0
        for i in self.config:
            if i==1:
                num+=1
        return num
    
    def off(self):
        '''
        returns number of 0 bits
        '''
        num=0
        for i in self.config:
            if i==0:
                num+=1
        return num
    
    def flip_site(self,i):
        '''
        flips bit at designated site
        '''
        self.config[i]=1-self.config[i]
    
    def int(self):
        '''
        returns values of bitstring in decimal
        '''
        value=0
        for (i,j) in enumerate(reversed(self.config)):
            if j == 1:
                value += 2**i
        return value
    
    def set_config(self, s:list[int]):
        '''
        creates list from bitstring
        '''
        self.config=list(s)
        
    def set_int_config(self, dec:int):
        '''
        sets bitstring given integer
        '''
        for i in range(len(self.config)):
            self.config[i] = dec % 2
            dec //= 2
        self.config = self.config[::-1]

