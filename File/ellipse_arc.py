from matplotlib import pyplot as plt
import math
sa=int(input("Enter starting angle :"))
ea=int(input("enter ending angle :"))
rx=int(input("Enter radius in x-axis : "))
ry=int(input("Enter radius in y-axis : "))
xc=int(input("Enter x-cordinate of centre : "))
yc=int(input("Enter y-cordinate of centre : "))
sa=sa*(math.pi /180)
ea=ea*(math.pi/180)
lx=[]
ly=[]
while(sa<=ea):
    lx.append(xc+rx*math.cos(sa))
    ly.append(yc+ry*math.sin(sa))
    sa+=0.1
plt.plot(lx,ly)
plt.xlim(-20,20)
plt.ylim(-20,20)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Ellipse arc drawing algorithm")
plt.show()
