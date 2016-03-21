def solution(N):
    # write your code in Python 2.7
    N=bin(N)
    gaps=[]
    gap_flag=0
    gap=""
    for n in str(N).replace("0b",""):
        gap+=n
        if n=="1":
            gap_flag+=1
        if gap_flag==2:
            gap_flag=1
            gaps.append(gap.strip())
            gap=n
    
    if len(gaps)>0:
        max_gap=gaps[0]
    for i,gap in enumerate(gaps):
        
        next=i+1
        if next<len(gaps):
           
            if len(max_gap)<len(gaps[next]):
                max_gap=gaps[next]
                print max_gap
    

      
    if len(gaps) >0:
        
        max_gap=max_gap.replace("1","")
        return len(max_gap)
    else:
        return 0
        
    
print solution(1041)