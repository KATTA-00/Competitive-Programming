#Test cases
t = int(input()) 

#Integer input
n = int(input()) 

#Tuple input
n,m,k = tuple(map(int,input().split()))

#List input
inplst = list(map(int,input().split()))

#Remove duplicates
inplst = list(set(map(int,input().split())))

#Line by line list
Nlst=[]
t = int(input())
for i in range(t):
    Nlst.append(int(input()))