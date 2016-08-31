def main():
    myencrypt=open("encryptedalphabet.txt", "r")
    encryptedalphabet=myencrypt.read() #The scrambled alphabet is read from file and placed in a variable
    myencrypt.close()
    themsg=open("unencryptedmessage.txt", "r") #The encrypted message was created in the encryption program.
    msg=themsg.read()
    themsg.close()
    alphabet=[""]*26 
    for c in range(26):
        alphabet[c] = chr(c+65) #This is the normal alphabet.
    encrypted_alphabet=[""]*26
    i=0 #counter for following for loop
    for c in encryptedalphabet:
        encrypted_alphabet[i]=c
        i+=1

    print("Your unencrypted message is: ", msg)
    
    print("Your encrypted message is: ", end="")
    encryptedMessage=""
    for c in msg.upper():
        b=0 #Counter for while loop
        if ord(c)<ord("A") or ord(c) > ord("Z"):
            print(c, end="") #non-letter characters are read through.
        else:
            while encrypted_alphabet[b]!=c:
                b+=1
            print(alphabet[b], end="")
            encryptedMessage+=alphabet[b]


    encrypted = open("encryptedmessage.txt", "w")
    encrypted.write(encryptedMessage)
    encrypted.close()
    print()
    print("The encrypted message was written to the disk.")

    

            

    
            
            
            
            

    
    


main()
