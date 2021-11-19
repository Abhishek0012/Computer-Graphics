from matplotlib import pyplot as plt
import math
theta=int(input("Enter starting angle :"))
theta = theta * (math.pi/180)
fi=int(input("Enter ending angle :"))
fi = fi * (math.pi/180)
x=int(input("Enter x coordinate of point of rotation :"))
y=int(input("Enter y coordinate of point of rotation :"))
r=int(input("Enter Radius : "))
lx=[]
ly=[]
while(theta<=fi):
    lx.append(x+r*math.cos(theta))
    ly.append(y+r*math.sin(theta))
    theta+=0.1
plt.plot(lx,ly)
plt.xlim(-20,20)
plt.ylim(-20,20)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("circle arc drawing algorithm")
plt.show()

