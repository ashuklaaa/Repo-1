import math
while True:
    print("Choose your operation:\n 1) Addition \n 2) Subtraction \n 3) Multiplication \n 4) Division \n 5) Floor division \n 6) modulus \n 7) percentage \n 8) Simple Interest")
    op=int(input())
    if op==1:
        print("How many numbers do you want to add?")
        n=int(input())
        l=list(map(int, input("Enter numbers: ").split()))
        print("your sum is ",sum(l))
    elif op==2:
        no=(int(input("Enter number 1 ")))
        nt=(int(input("Enter number 2 ")))
        d= no-nt
        print("your difference is ",d)
    elif op==3:
        print("How many numbers do you want to multiply?")
        n=int(input())
        l=list(map(int, input("Enter numbers: ").split()))
        print("your product is",math.prod(l))
    elif op==4:
        no=(int(input("Enter number 1 ")))
        nt=(int(input("Enter number 2 ")))
        q=no/nt
        print("your answer is ",q)
    elif op==5:
        no=(int(input("Enter number 1 ")))
        nt=(int(input("Enter number 2 ")))
        q=no//nt
        print("your answer is ",q)
    elif op==6:
        no=(int(input("Enter number 1 ")))
        nt=(int(input("Enter number 2 ")))
        r=no%nt
        print("your answer is ",r)
    elif op==7:
        no=(int(input("Enter number 1 ")))
        nt=(int(input("Enter number 2 ")))
        p=(no/nt)*100
        print("your answer is ",p)
    elif op==8:
        p=(int(input("Enter principle ")))
        r=(int(input("Enter rate of interest ")))
        t=(int(input("Enter time period ")))
        s=(p*r*t)/100
        print("your answer is ",s)
    else:
        break
    
    
