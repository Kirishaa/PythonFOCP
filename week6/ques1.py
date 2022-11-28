
def dec_bin():
    user = int(input("Enter a positive integer: "))
    binary = []
    while (user>0):
        b=user%2
        binary.append(b)
        user=user//2
    binary.reverse()
    for i in binary:
        print(i, end=" ")

dec_bin()