import random

def main():
    encrypt=["*"]*26   
    print(encrypt)

    print("Alphabet:  ", end="")
    for n in range(26):
        letter = chr(n+65)
        
        print(letter, end="")

        notfound = True
        while notfound:
            possible_position = random.randint(0,25)
            if encrypt[possible_position] == "*":
                notfound = False
        encrypt[possible_position] = letter

    print("\nScrambled: " , end="")
    for n in range(26):
        print(encrypt[n], end="")

    print("\n\n")

    alphabet=""
    msg=input("Please enter your encrypted message: ")
    for n in range(26): #It now begins the process for writing the encrypted alphabet to the disk.
        alphabet+=encrypt[n]
    alphabet_file=open("encryptedalphabet.txt", "w")
    alphabet_file.write(alphabet)
    alphabet_file.close()
    print("The encrypted alphabet was written to the disk.")
    msg_file=open("unencryptedmessage.txt", "w") #The program also writes the encrypted message to the disk.
    msg_file.write(msg)
    msg_file.close()
    print("The unencrypted message was written to the disk.")

main()
