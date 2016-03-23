def solution(A):
    # write your code in Python 2.7
    A=sorted(A)
 
    if not A:
        return 1
    
    if 1 not in A:
        return 1
    if len(A)==1:
        
        return A[0]+1
    for i in range(0,len(A)-1):
         
        if (A[i+1]-A[i]) !=1:
            return A[i]+1
            
    return A[i+1]+1
