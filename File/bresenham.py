# Write a prohram to implement bresnham's line drawing algorithm considering abs(delx) > abs(del) y (else do same for y)
from matplotlib import pyplot as plt
x1=int(input("Enter x1: ")) 
y1=int(input("Enter y1: ")) 
x2=int(input("Enter x2: ")) 
y2=int(input("Enter y2: ")) 
dy = abs(x2-x1)
dx=  abs(y2-y1)
lx=[]
ly=[]
p = 2*dy-dx
while(x1<=x2):
    lx.append(x1)
    ly.append(y1)
    if p<0 :
        p=p+2*dy
    else:
        p=p+2*dy-dx
        y1+=1
    x1+=1
plt.plot(lx,ly)
plt.xlim(0,200)
plt.ylim(0,200)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Bresenham's Line Drawing Algorithm")
plt.show()

    
