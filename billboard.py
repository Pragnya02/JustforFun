'''
PRAGNYA SRINIVASAN
01453947
'''

import sys
def bill():
    L= int(raw_input("Enter the length L "))
    n= int(raw_input("Enter the possible number of points "))
    x=map(int,raw_input("Enter all the location values ").split())
    if x[n-1] <= L:
        print "Continuing..."
    else:
        print "Exceeds the limit. Start again"
        print " "
        sys.exit()    
    r=map(int,raw_input("Enter all the revenues for above location ").split())
    M=[]
    p=[]
    indexx=[]
    for i in range(0,n):
        p.append(0)
        M.append(0)
        indexx.append(' ')
    for i in range(0,n):
        for j in range(i+1,n):
            if(x[j]-x[i] > 5):
                p[j] =max(p[j],i+1)
   
    print "P[j]: ",p
    print " "
    M[-1] = 0
    
    for j in range(0,n):
        M[j]=max(M[p[j]-1]+r[j], M[j-1])
        if(M[p[j]-1]+r[j] > M[j-1]):
            ind= M.index(M[p[j]-1])
            indexx[j]= str((indexx[ind])) + " " + str(j+1)  
            print "M[",j+1,"]: ",M[j] 
            print "Chosen Points:",indexx[j]
            print " "                          
        else:
            indexx[j]= str(indexx[j-1])
            print "M[",j+1,"]: ",M[j]  
            #M[j]= M[p[j]]+r[j]
            print "Chosen Points: ",indexx[j]
    print " "        
    print "------------------------------------------"        
    print "j     M[j]           indexx[j]"
    for j in range(0,n):
        indexx[j]="[" + (indexx[j].strip(' ')) + "]"
        print '%d %8d%19s' %(j,M[j],indexx[j])
           
    print " "   
    print "Maximum Revenue: ",max(M)
    print 'Points chosen %5s' %indexx[n-1]
               
bill() 