x11=int(input())
l=list(map(int,input().split()))
z11=0
for i in range(0,x11-1):
	for j in range(i+1,x11):
		u11=l[j]-l[i]
		if u11<0:
			u11=u11*-1
		if u11>z11:
			z11=u11
print(z11)
