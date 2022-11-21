import sys
if bool(sys.argv[1:])==True:
    count = len(sys.argv)
    total = 0
    while count > 1:
        count -= 1
        total += float(sys.argv[count])
    print("The average is:", total/len(sys.argv[1:]))
    print("Total is", total)
else:
    print("No arguments were provided.")
