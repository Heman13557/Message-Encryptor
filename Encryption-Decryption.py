
def Encryption(val):
    a=0
    val1=""
    for i in  range(0,len(val)):
        a=ord(val[i])
        if(a!=32):
            if(i%5==1):
                a+=5
            if(i%5==2):
                a+=4        
            elif(i%5==3):
                a+=3       
            elif(i%5==4):
                a+=2
            elif(i%5==0):
                a+=6
        else:
            a+=1
        val1=val1+chr(a)
    print(val1)


def Decryption(val):
    a=0
    val1=""
    for i in  range(0,len(val)):
        a=ord(val[i])
                
        if(a!=33):
            if(i%5==1):
                a-=5
            if(i%5==2):
                a-=4        
            elif(i%5==3):
                a-=3       
            elif(i%5==4):
                a-=2
            elif(i%5==0):
                a-=6
        else:
            a-=1
        
        
        val1=val1+chr(a)
    print(val1)


value = input("Type your message you want to get encrypted :")
Decryption(value)