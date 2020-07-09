top=None
s=[]
def push(s,N):
    s.append(N)
    top=len(s)-1

def pop_(s):
    if s==None:
        return "Underflow"
    else:
        i=s.pop()
        if len(s)==0:
            top=None
        else:
            top=len(s)-1

def peek(s):
    if s!=[]:
        top=len(s)-1
        return(s[top])
    else:
        print("STACK is empty")

def dis_play(s):
    if s!=[]:
        top=len(s)-1
        print(s[top],"<-")
        for i in range (top-1,-1,-1):
            print(s[i])
    else:
        print("STACK is empty")

def main():
    print("\nWelcome to STACK functions:")
    print("1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("4. DISPLAY")
    print("5. EXIT")
    ch=int(input("Enter your choice"))
    if ch==1:
        n=int(input("\nEnter item to be pushed:"))
        push(s,n)
        print("One item added in stack.")
        main()
    elif ch==2:
        pop_(s)
        print("One item deleted from STACK")
        main()
    elif ch==3:
        val=peek(s)
        print("Value at PEEK of stack is:",val)
        main()
    elif ch==4:
        print("STACK is as follows:")
        dis_play(s)
        main()
    elif ch==5:
        print("Exiting...Thank you...")
        return None
main()
