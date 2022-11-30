def int_prime():  
    user = int(input("Enter a number: "))
    output = False
    if user<=1:
        output=True
    if user>1:
        for i in range(2,user):
            if (user%i)==0:
                output = True
                break
    if output:
        print (f"{user} is not prime number.")
    else:
        print(f"{user} is prime number.")

int_prime()
    