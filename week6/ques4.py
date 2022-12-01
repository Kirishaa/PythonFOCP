def encrypt():
    user = input("Enter your message: ")
    no_space= user.replace(" ","")
    reversee = no_space[::-1]
    print(reversee)

encrypt()