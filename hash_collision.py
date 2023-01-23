import hashlib
import os
import string
import random

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here
    bits = 1 << k
    letters = string.ascii_letters
    for i in range(0,2^k):    
      string_1 =  ''.join(random.choice(letters) for i in range(k+1) )
      hashcode_1 = hashlib.sha256(string_1.encode('utf-8')).hexdigest()
      hashcode_bi_1 = bin(int(hashcode,16)& (bits - 1))

      string_2 =  ''.join(random.choice(letters) for i in range(k+1) )  
      hashcode_2 = hashlib.sha256(string_2.encode('utf-8')).hexdigest()
      hashcode_bi_2 = bin(int(hashcode,16)& (bits - 1))
      
      if hashcode_bi_1 == hashcode_bi_2:
        return (string_1.encode('utf-8'), string_2.encode('utf-8'))
        #print(string_1, string_2)

    x = b'\x00'
    y = b'\x00'
    #print('Did not found matching')
    return( x, y )