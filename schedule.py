'''
*Scheduling Algorithm - Triatholon
*

'''

def mergesort(swimmingtime,bottom,top):
    N=top-bottom;
    if N<=1:
        return
    mid=bottom+ N/2
    mergesort(swimmingtime,bottom,mid);
    mergesort(swimmingtime,mid,top);
    temp=[];
    i=bottom;
    j=mid;
    for k in range(0,N):
        if i==mid:
            
            temp.append(swimmingtime[j])
            j+=1
        elif j==top:
            
            temp.append(swimmingtime[i]);
            i+=1
            
        elif swimmingtime[j]<swimmingtime[i]:
            
            temp.append(swimmingtime[j])
            j+=1
        else:
            temp.append(swimmingtime[i])
            i+=1
    print "after sorting:"
    for k in range(0,N):
        swimmingtime[bottom + k]= temp[k];
        print swimmingtime[bottom+ k ]
        
def schedule():
   #newswimming_time[],newbiking_time[],newracing_time[],oldswimming_time[],oldikingtime[],oldracing_time[],start_time[],finish_time[]
   #take user input for n
    oldswimming_time=[]
    oldbiking_time=[]
    oldracing_time=[]
    newswimming_time=[]
    newbiking_time=[]
    newracing_time=[]
    start_time=[]
    finish_time=[]
    total_time=[]
    
    n=int(input("Enter the number of Racers"));
    
    for i in range(0,n):
        oldswimming_time.append(int(input("Enter the swimming time for 1 Racer and press Enter")))
        oldbiking_time.append(int(input("Enter the biking time for 1 Racer and press Enter")))
        oldracing_time.append(int(input("Enter the racing time for 1 Racer and press Enter")))
    
    newswimming_time=list(oldswimming_time)
    newbiking_time=list(oldbiking_time)
    newracing_time=list(oldracing_time)
    
    for i in range (0,n):
        start_time.append(int(0));
        finish_time.append(int(0));
        total_time.append(int(0));
    #do sort here
    mergesort(newswimming_time,0,n);
    
    for i in range(0,n):
        print "New Swimmingtime: ",newswimming_time[i]
    for i in range(0,n):
        for j in range(0,n):
            if newswimming_time[i]==oldswimming_time[j]:
                newbiking_time[i]=oldbiking_time[j];
                newracing_time[i]=oldracing_time[j];
    
    finish_time[0]=start_time[0]+oldswimming_time[0];
    print "Start time of Racer0: ",start_time[0]," ","Finish time of Racer0: ",finish_time[0]
        
    for i in range(1,n):
        start_time[i]=finish_time[i-1]
        finish_time[i]=start_time[i]+newswimming_time[i]
        
        print "Start time of Racer",i,": ",start_time[i]," ","Finish time of Racer",i,": ",finish_time[i]
    max=0
    for i in range(0,n):
        total_time[i]=newswimming_time[i]+newbiking_time[i]+newracing_time[i]
        if max<total_time[i]:
            max=total_time[i]
    
    print "Completion Time",max
schedule();    

