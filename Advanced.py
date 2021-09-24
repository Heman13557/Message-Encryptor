
import random
def Encryption(val):
    key = []
    k=0
    a=0
    val1=""
    for i in range(0,5):
        k = random.randint(1,10)
        key.append(k)
    key.append(1)
    for i in  range(0,len(val)):
        
        a=ord(val[i])
        if(a!=32):
            if(i%5==1):
                
                a+=key[0]
            elif(i%5==2):
                
                a+=key[1]                       
            elif(i%5==3):
                
                a+=key[2]                
                       
            elif(i%5==4):
                
                a+=key[3]
            elif(i%5==0):
                
                a+=key[4]
        else:
            
            a+=key[5]
        
        val1=val1+chr(a)
    print("Encrypted Message : ",val1)
    print("Key for Decryption : ",key)

def Decryption(val,key):
    a=0
    val1=""
    for i in  range(0,len(val)):
        a=ord(val[i])
                
        if(a!=33):
            if(i%5==1):
                
                a-=key[0]
            elif(i%5==2):
                
                a-=key[1]                       
            elif(i%5==3):
                
                a-=key[2]                
                       
            elif(i%5==4):
                
                a-=key[3]
            elif(i%5==0):
                
                a-=key[4]
        else:
            
            a-=key[5]
        val1=val1+chr(a)
    print(val1)


value = input("Type your message you want to get encrypted :")
Encryption(value)
msg = input("Type your message you want to get encrypted :")
print("Enter Encryption Key Numbers one by one :")
key = []
v=0
for i in range(6):
    v = int(input("Enter Key Number "+str(i+1)+" :"))
    key.append(v)
Decryption(msg,key)
