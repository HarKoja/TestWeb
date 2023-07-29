pas=int(input("What's your password? "))
if pas==4216:
    while True:
        print("1)Sets\n2)Checknumber\n")
        menu=input("What do you want to do? ")
        if menu == "1":
            s = set()
            print("alright , Sets!")
            for i in range (20):
                print("for Removing : rm  for Adding : add  for counting : cn  for Exit : ex")
                Sets1=input("Let's see : ")
                print(s)
                if Sets1=="add":
                    Adding=input("Add What? ")
                    s.add(Adding)
                    print(s)
                elif Sets1=="rm":
                    print(s)
                    Removing=input("Remove What? ")
                    s.remove(Removing)
                    print(s)
                elif Sets1=="cn":
                    print(f"The set have {len(s)} elements")
                elif Sets1 == "ex":
                    break
            else:
                print("Invalid Data!")
        elif menu == "2":
            print("alright , Checknumber!")
            Check1=int(input("What's x? "))
            if Check1%2==0:
                print("even")
            elif Check1%2!=0:
                print("odd")
            else:
                print("Invalid Data!")
else:
    print("Invalid Password!")