import sys

Input = ""
CipherType = ""
ProcessType = ""
InputFile = ""
OutputFile = ""

lis = []
lis = list(sys.argv)

lis.append(0)
CipherType = lis[1]
ProcessType = lis[2]
InputFile = lis[3]
OutputFile = lis[4]
k1 = lis[5]
k2 = lis[6]
f=open(InputFile, "r")
if f.mode == 'r':
    Input = f.read()
def vigenere(type):
    output = ''
    if type[0] == 'e':
            idx = 0
            for i in Input:  
                idx %= len(k1)
                if i.isalpha() == False : 
                    output += i
                    continue
                elif i.islower() :
                    output += chr(((ord(i)-97+ord(k1[idx])-97)%26)+97)
                else : 
                    output += chr(((ord(i)-65+ord(k1[idx])-65)%26)+65)
                idx = idx+1
                
    else:
        idx = 0
        for i in Input:
            idx %= len(k1)
            if i.isalpha() == False : 
                    output += i
                    continue
            elif i.islower() :
                output += chr(((ord(i)-97-ord(k1[idx])-97+26)%26)+97)
            else : 
                output += chr(((ord(i)-65-ord(k1[idx])-65+26)%26)+65)
            idx = idx+1

    return output

def affine(type):
    output = ''
    key1=int(k1)
    key2=int(k2)
    if type[0] == 'e':
           
            for i in Input:  
                if i.isalpha() == False : 
                    output += i
                    continue
                elif i.islower() :
                    output += chr( ( (ord(i) - 97 ) * key1 + key2 ) %26+97)
                else : output += chr( ( (ord(i) - 65 ) * key1 + key2 ) %26+65)
                 
    else:
        inv = 0
        for i in range(1,26):
            if  ( i * key1  ) % 26 == 1 :
                inv = i
                break
        
        for i in Input:
            if i.isalpha() == False : 
                    output += i
                    continue
            elif i.islower() :
                 output += chr( ( inv * ( ( ord(i) - 97 )- key2 )+26 ) %26+97)
            else :  output += chr( ( inv * ( ( ord(i) - 65 )- key2 )+26 ) %26+65)

    return output

def shift(type):
    output = ''
    key1=int(k1)
    if type[0] == 'e':
            for i in Input:  
                if i.isalpha() == False : 
                    output += i
                    continue
                elif i.islower() : 
                    output += chr( ( (ord(i) - 97 ) + key1 ) %26+97)
                else : output += chr( ( (ord(i) - 65 ) + key1 ) %26+65)
                
    else:
        for i in Input:
            if i.isalpha() == False : 
                    output += i
                    continue
            elif i.islower() : 
                output += chr( ( (ord(i) - 97 )- key1+26 ) %26+97)
            else : output += chr( ( (ord(i) - 65 )- key1+26 ) %26+65)
                        
    return output

output = ""

if CipherType == 'affine' :
    output = affine(ProcessType)
elif CipherType == 'vigenere' :
    output = vigenere(ProcessType)
else : output = shift(ProcessType)
f = open(OutputFile,"w+")
f.write(output)
f.close()

  