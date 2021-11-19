# Write a program to implement dda algorithm
from matplotlib import pyplot as plt
x1=int(input("Enter x1: ")) 
y1=int(input("Enter y1: ")) 
x2=int(input("Enter x2: ")) 
y2=int(input("Enter y2: ")) 
dx=x2-x1 
dy=y2-y1
m=dy/dx
lx=[]
ly=[]
while(x1<=x2):
    lx.append(x1)
    ly.append(y1)
    x1=x1+1
    y1=y1+m*dx
plt.plot(lx,ly)
plt.xlim(0,200)
plt.ylim(0,200)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("DDA Line Drawing Algorithm")
plt.show()
