class CircularQueue: 
    def __init__(CQ): #Constructor 
        CQ.queue = [None]*7 # Create a list with None values with the size 7 
        CQ.front = -1 
        CQ.rear = -1 
        CQ.maxSize = 7 
            
    def C_enqueue(CQ,data): #Adding elements to the queue 
        if (CQ.rear+1)%CQ.maxSize==CQ.front: 
            CQ.rear=-1 
            CQ.rear = (CQ.rear + 1) % CQ.maxSize 
            CQ.queue[CQ.rear]=data 
        elif CQ.front== -1: 
            CQ.front=0 
            CQ.rear=0 
            CQ.queue[CQ.rear]=data 
        else: 
            CQ.rear = (CQ.rear + 1) % CQ.maxSize 
            CQ.queue[CQ.rear]=data 
    def C_dequeue(CQ): #Removing elements from the queue 
        if CQ.front==-1: 
            print("Queue is empty") 
        elif CQ.front==CQ.rear: 
            CQ.queue.pop(CQ.front) 
            CQ.front=CQ.front+1 
        else: 
            CQ.queue.pop(CQ.front) 
            CQ.front = (CQ.front + 1) % CQ.maxSize 
    q = CircularQueue() 
    print("MENU BASED CIRCULAR QUEUE") 
    cd=True 
    while cd: 
        print("1. ENQUEUE") 
        print("2. DEQUEUE") 
        print("3. DISPLAY ") 
        print("4. Front Position ") 
        print("5. Rear Position ") 
        choice=int(input("Enter your choice (1-5) : ")) 



        if choice==1: 
            val=input("Enter the element: ") 
            q.C_enqueue(val) 
        elif choice==2: 
            q.C_dequeue() 
        elif choice==3: 
            print(q.queue) 
        elif choice==4: 
            print("Front element position :", q.front) 
        elif choice==5: 
            print("Rear element position : ", q.rear) 
        else: 
            print("You entered invalid choice: ") 
        print("Do you want to continue? Y/N") 
        option=input( ) 
        if option=='y' or option=='Y': 
            cd=True 
        else: 
            cd=False 

