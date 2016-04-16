"""
1. Version
procedure bubbleSort( A : list of sortable items )
    n = length(A)
    repeat
       newn = 0
       for i = 1 to n-1 inclusive do
          if A[i-1] > A[i] then
             swap(A[i-1], A[i])
             newn = i
          end if
       end for
       n = newn
    until n = 0
end procedure
"""
A=[5, 1, 4, 2, 8,0]
n=len(A)
swapped =True
iteration=0
while (swapped):
  swapped=False
  iteration+=1
  for i in range(1,n):
    iteration+=1
    if A[i-1] >A[i]:
      temp=A[i]
      A[i]=A[i-1]
      A[i-1]=temp
      swapped=True


print "1. Version solution: "+str(A)
print "Number of iterations: "+str(iteration)
#1. Version solution: [0, 1, 2, 4, 5, 8]
#Number of iterations: 36

"""
2. Version
procedure bubbleSort( A : list of sortable items )
    n = length(A)
    repeat
       swapped = false
       for i = 1 to n-1 inclusive do
          if A[i-1] > A[i] then
             swap(A[i-1], A[i])
             swapped = true
          end if
       end for
       n = n - 1
    until not swapped
end procedure

"""

A=[5, 1, 4, 2, 8,0]
n=len(A)
iteration=0
swapped =True
while (swapped):
  iteration+=1
  swapped=False
  for i in range(1,n):
    iteration+=1
    if A[i-1] >A[i]:
      temp=A[i]
      A[i]=A[i-1]
      A[i-1]=temp
      swapped=True
  n=n-1
  

print "2.Version  solution: "+str(A)
print "Number of iterations: "+str(iteration)
#2.Version  solution: [0, 1, 2, 4, 5, 8]
#Number of iterations: 21
