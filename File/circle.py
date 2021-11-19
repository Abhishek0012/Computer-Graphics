from matplotlib import pyplot as plt
r = int(input("Enter radius : "))
xc = int(input("x center : "))
yc = int(input("y center : "))
p = 5/4 - r
x = 0 
y=r 
lx=[]
ly=[]
while(x<=y):
    lx.append(x+xc)
    ly.append(y+yc)
    lx.append(y+xc)
    ly.append(x+yc)
    lx.append(-x+xc)
    ly.append(y+yc)
    lx.append(x+xc)
    ly.append(-y+yc)
    lx.append(-x+xc)
    ly.append(-y+yc)
    lx.append(-y+xc)
    ly.append(x+yc)
    lx.append(y+xc)
    ly.append(-x+yc)
    lx.append(-y+xc)
    ly.append(-x+yc)
    if p<0 :
        p= p + 2*x - 3
    else :
        p= p + 2*x-2*y + 5
        y-=1
    x+=1
plt.plot(lx,ly)
plt.xlim(-200,200)
plt.ylim(-200,200)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Mid point circle drawing algorithm")
plt.show()
