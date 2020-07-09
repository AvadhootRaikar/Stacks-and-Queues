front=None
rear=None
Queue=[]

def Qinsert(Queue,N):
    Queue.append(N)
    if len(Queue)==1:
        front=rear=0
    else:
        rear=len(Queue)-1
    
def Qdelete(Queue):
    if Queue==[]:
        print("UnderFlow")
    else:
        item=Queue.pop(0)
        if len(Queue)==0:
            front=rear=None
            
def Qpeek(Queue):
    if Queue!=[]:
        front=0
        return(Queue[front])
    else:
        print("QUEUE IS EMPTY...")

def Qdisplay(Queue):
    if len(Queue)==1:
        print(Queue[0],"<=")
    elif Queue!=[]:
        front=0
        rear=len(Queue)-1
        print(Queue[front],"<-")
        for i in range(front+1,rear,1):
            print(Queue[i])
        print(Queue[rear],"<-")
    else:
        print("QUEUE IS EMPTY..")

def Qmain():
    print("\n*WELCOME TO QUEUE OPERATIONS*")
    print("1. INSERT")
    print("2. DELETE")
    print("3. PEEK")
    print("4. DISPLAY")
    print("5. EXIT")
    ch=int(input("ENTER YOUR CHOICE(1-5) :"))
    if ch==1:
        x=int(input("\nEnter item to be inserted into queue :"))
        Qinsert(Queue,x)
        print("One item added in Queue.")
        Qmain()
    elif ch==2:
        Qdelete(Queue)
        print("One item deleted from Queue")
        Qmain()
    elif ch==3:
        val=Qpeek(Queue)
        print("Value at Peek of Queue is :",val)
        Qmain()
    elif ch==4:
        print("QUEUE IS AS FOLLOWS:")
        Qdisplay(Queue)
        Qmain()
    elif ch==5:
        print("Exiting...Thank you...")
        return None
    else:
        print("You have entered a wrong choice. Try Again")
        Qmain()
Qmain()
    
    
    
