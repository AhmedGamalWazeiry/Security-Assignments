Challenge Name ==> genfei
________________________________________

Challenge Description :
-----------------------

We found an encrypted secret and an encrypting machine. It seems to be a complicated cipher.

________________________________________

The main idea :
---------------
1) a^b =c if c^a=b then c^b=a

2) If we notice in the file encryp.py all equation in encrypt funcation Depends on the XOR operation and i can use the first step to decrypt this. 

3) In decrypt function i reversed the two equations which exists in encrypt function because of decryption is a reverse order of encryption.

4) So the first step of decryption in decrypt function :
    -  get d2 using d3.          (d2= d1^1337)
    -  get a2 using c3,d2.       (a2 = c3 ^ (F(d2 | F(d2) ^ d2)))
    -  get b2 using b3,d2,a2.    (b2 = b3 ^ (F(d2 ^ F(a2) ^ (d2 | a2))))
    -  get c2 using a3,d2,a2,b2. (a3^ (F(d2 | F(b2^ F(a2)) ^ F(d2 | b2) ^ a2)))

5) So the first step of decryption in decrypt function:
    -  get a1 using d2             (a1 = d2 ^ 31337)
    -  get d1 using c2,a1          (d1 = c2 ^ (F(a1 | F(a1) ^ a1)))
    -  get c1 using b2,a1,d1       (c1 = b2 ^ (F(a1 ^ F(d1) ^ (a1 | d1))))
    -  get b1 using a2,a1,d1,c1    ( b1 =  a2 ^ (F(a1 | F(c1 ^ F(d1)) ^ F(a1 | c1) ^ d1)))
 
6) After decryption all characters in the flag file remove all (#) characters
  
