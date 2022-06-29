import numpy as np
import math

val = (input("Enter your value for the arry size: "))
P = (input("Enter number of processors: "))

if  val%P== 0 :
        mod = val%P
        VN = val + val%P
        X = np.zeros((VN))
        for i in range(len(X)):
                if i>= VN -mod : X[i]=None
                else: X[i] = i+1

elif  P%2 == 0  : 
        v = val + (P - (val %P)) 
        mod = v%P 
        VN = v  + mod
        X = np.zeros((VN))
        for i in range(len(X)):
                if i>= VN -(P - (val %P)) -mod: X[i] =None
                else: X[i] = i+1

elif  P%2 != 0 : 
        val = val
        mod = val%P
        VN = val + 2 * (P -(val %P)) + mod
        X = np.zeros(VN)
        for i in range(len(X)):
                if i>= VN - (2*(P - (val %P))) - mod : X[i]= None
                else: X[i] = i + 1

        
print('X=',X)

NB = int(math.ceil(len(X)/float(P)))

print('NB=', NB)

pb = [[]] * P


for i in range(P):
        pb[i] = []


for i in range(len(X)):
        for j in range(P):
                k=math.trunc(i/NB)
#        print('k =', k)
                if k == j:
                        pb[j].append(X[i])


for i in range(P):
        print('pb[',i,']',pb[i])

pc = [[]] * P

for i in range(P):
        pc[i] = []



for i in range(len(X)):
        for j in range(P):
                k=math.trunc(i%P)
#        print('i=', i, 'k=', k)
                if k==j:
                        pc[j].append(X[i])

for i in range(P):
        print('pc[',i,']',pc[i])

#for j in range(P):
M= pb
N= pc

R = np.zeros((P,NB))
S = np.zeros((P,NB))

print("M=", M)
print("N=", N)

# iterate throught rows
for i in range(len(M)):
    # iterate through columns
    for j in range(len(M[0])):
        k=math.trunc((j+i*NB)%P)
        r=math.trunc((j+i*NB)/P )
        print('i',i, 'j', j, 'k =', k, 'r =', r)
#        if j>= val%4 : N[k][r]==0
        print(M[i][j], N[k][r])
        R[i][j] = N[k][r]

print('In R the N cyclic distibution of X is converted to the block distribution of X')
print('R=', R)

for i in range(len(N)):
        for j in range(len(N[0])):
                if P%10 == 0:
                        k = math.trunc((j/(float(NB)/(P))) + (-1)**(NB) * (i/float(NB)) )
                        r = math.trunc(j%(float(NB))*P +(-1)**(NB)* (i%(NB)))%NB
                        
                elif ((len(X))/P) % 2 != 0  :
                        k = math.trunc((j/(float(NB)/(P))) + (-1)**(NB-1) * (i/float(NB)) )
                        r = math.trunc(j%(float(NB)/(P))*P +(-1)**(NB-1)* (i%(NB)))%(NB)                        
                else: 
                        k = math.trunc((j/(float(NB)/(P))) + (-1)**(NB) * (i/float(NB)) )
                        r = math.trunc(j%(float(NB)/(P))*P +(-1)**(NB)* (i%(NB)))%NB

                print('i', i, 'j', j, 'k=', k, 'r=', r)
                print(N[i][j], M[k][r])
                S[i][j] = M[k][r]

print('In S the M block distibution of X is converted to the cyclic distribution of X')
print('S=',S)    
