from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from mpl_toolkits.mplot3d import axes3d as ax3d
from matplotlib import animation
import math
import sys

mag_field = np.random.randint(low= 1 , high= 100, size = 1000)
magVectorOxygen=[1,1,1]
magVectorHydrogen=[1,1,1]
magVector1=[None]*2
larmorFreqHydrogen =42.6*mag_field
larmorFreqOxygen = 5.8*mag_field


def decayVector(angle):
    xVectorOxygen=[]
    yVectorOxygen=[]
    zVectorOxygen=[]
    xyVectorOxygen=[]
    xVectorHydrogen=[]
    yVectorHydrogen=[]
    zVectorHydrogen=[]
    xyVectorHydrogen=[]
    timeVector=[]
    angleVector=[]
    magVector1Oxygen=[None]*3
    magVector1Hydrogen=[None]*3
    magVectorXYOxygen=[None]*3
    magVectorXYHydrogen=[None]*3
    t=0
    magVectorXYOxygen[0]=magVectorOxygen[0]*math.cos(angle)
    magVectorXYOxygen[1]=magVectorOxygen[1]*math.cos(angle)
    magVectorXYOxygen[2]=magVectorOxygen[2]*math.cos(angle)
    magVectorXYHydrogen[0]=magVectorHydrogen[0]*math.cos(angle)
    magVectorXYHydrogen[1]=magVectorHydrogen[1]*math.cos(angle)
    magVectorXYHydrogen[2]=magVectorHydrogen[2]*math.cos(angle)
    j =0 
    while(magVector1Hydrogen[0]!=0 or magVector1Hydrogen[1]!=0):
        
        E1 = math.exp(-t/100)
        E2 = math.exp(-t/600)
        A= np.array([[E2,0,0],[0,E2,0],[0,0,E1]])
        B= np.array([0, 0, 1-E1])
        phiHydrogen =2*math.pi*larmorFreqHydrogen[j]*t/1000
        phiOxygen =2*math.pi*larmorFreqOxygen[j]*t/1000
        angDiff=phiHydrogen -phiOxygen
        angleVector.append(angDiff)
        RzOxygen=np.array([[math.cos(phiOxygen),-math.sin(phiOxygen),0],[math.sin(phiOxygen),math.cos(phiOxygen),0],[0, 0, 1]])
        RzHydrogen=np.array([[math.cos(phiHydrogen),-math.sin(phiHydrogen),0],[math.sin(phiHydrogen),math.cos(phiHydrogen),0],[0, 0, 1]])
        AfbHydrogen = np.matmul(A,RzHydrogen)
        AfbOxygen = np.matmul(A,RzOxygen)
        magVector1Hydrogen =np.matmul(AfbHydrogen,magVectorXYHydrogen)+B
        magVector1Oxygen =np.matmul(AfbOxygen,magVectorXYOxygen)+B
        xVectorOxygen.append(magVector1Oxygen[0])
        xVectorHydrogen.append(magVector1Hydrogen[0])
        yVectorOxygen.append(magVector1Oxygen[1])
        yVectorHydrogen.append(magVector1Hydrogen[1])
        zVectorOxygen.append(magVector1Oxygen[2])
        zVectorHydrogen.append(magVector1Hydrogen[2])
        xyVectorOxygen.append(np.sqrt(np.square(magVector1Oxygen[0])+np.square(magVector1Oxygen[1])))
        xyVectorHydrogen.append(np.sqrt(np.square(magVector1Hydrogen[0])+np.square(magVector1Hydrogen[1])))
        timeVector.append(t)
        t = t+1
        if(j<999):
            j = j +1
        else:
            j=0
    oxygenVector=[xVectorOxygen,yVectorOxygen,zVectorOxygen,xyVectorOxygen,timeVector,angleVector]
    hydrogenVector=[xVectorHydrogen,yVectorHydrogen,zVectorHydrogen]
    vector = [oxygenVector,hydrogenVector]
    return vector



def init():
    for line in lines:
        line.set_data([],[])
        line.set_3d_properties([])
    return lines

def animate(i):
    A1 = xH[:i]
    B1 = yH[:i]
    C1 = zH[:i]

    A2 = xO[:i]
    B2 = yO[:i]
    C2 = zO[:i]

    xlist = [A1, A2]
    ylist = [B1, B2]
    zlist = [C1, C2]
    
    for lnum,line in enumerate(lines):
        line.set_data(xlist[lnum], ylist[lnum])
        line.set_3d_properties(zlist[lnum])
    return lines


def init1():
    line1.set_data([],[])
    return line1,

def animate1(i):
    x = time[:i]
    y = angleDifferance[:i]
    xmin, xmax = ax1.get_xlim()
    ymin, ymax = ax1.get_ylim()
    if i>0:
        if max(x) >= xmax:
            ax1.set_xlim(xmin, 2*xmax)
            ax1.figure.canvas.draw()
        if max(y) >= ymax:
            ax1.set_ylim(ymin, 2*ymax)
            ax1.figure.canvas.draw()
    
    line1.set_data(x, y)
    return line1,



waterMolcule= decayVector(float(sys.argv[1]))
Oxygen = waterMolcule[0]
Hydrogen = waterMolcule[1]

xO=Oxygen[0]
yO=Oxygen[1]
zO=Oxygen[2]
xH = Hydrogen[0]
yH = Hydrogen[1]
zH = Hydrogen[2]
time=Oxygen[4]
angleDifferance=Oxygen[5]
N=len(xH)


fig1 = plt.figure(2)
ax1 = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line1, = ax1.plot([], [], lw=2)
ax1.set_xlabel("time")
ax1.set_ylabel("differanceInAngularFreq")
anim1 = animation.FuncAnimation(fig1, animate1,init_func=init1, frames=N , interval=10, blit=False)
# anim.save("mag1.gif")

fig = plt.figure(1)
ax = ax3d.Axes3D(fig)
line, = ax.plot([], [], lw=2, linestyle= "-")

ax.set_xlim(min(xH),max(xH))
ax.set_ylim(min(yH),max(yH))
ax.set_zlim(min(zH),max(zH))
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.text2D(0, 0, "NonUniform Magnetic Field", transform=ax.transAxes)

plotlays, plotcols = [2], ["red","blue"]
lines = []
for index in range(2):
    lobj = ax.plot([],[],lw=2,color=plotcols[index])[0]
    lines.append(lobj)
anim = animation.FuncAnimation(fig, animate,init_func=init, frames=N , interval=10, blit=False)
# anim.save("mag.gif")
plt.show()
