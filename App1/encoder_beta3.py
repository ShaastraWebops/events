import time
import matplotlib.pyplot as plt
import numpy as np
plt.ion()

class encoder:
    r=31.0
    time=0
    def __init__(self,px=0,py=0,ptheta=0):
        self.x=px
        self.y=py
        self.theta=ptheta
        
    def loco(self,v1,v2,v3,sec):
        vx=(-v1*np.sin(np.pi/6))+(-v2*np.sin(np.pi/6))+v3
        vy=(v1*np.cos(np.pi/6))+(-v2*np.cos(np.pi/6))
        w=(v1+v2+v3)/self.r

        for t in range(1,2,1):
            dt=0.01
            for i in range(0,int(sec/dt),1):
                self.theta+=w*dt
                dx=vx*dt
                dy=vy*dt
                self.x+=-(dy*np.sin(self.theta))+(dx*np.cos(self.theta))
                self.y+=(dy*np.cos(self.theta))+(dx*np.sin(self.theta))
                self.time+=dt
                self.graph_plot()

    def graph_plot(self):
        plt.subplot(211)
        plt.axis([-10,10,-10,10])
        plt.plot(self.x,self.y,'b.')
        plt.subplot(212)
        plt.plot(self.time,self.theta*180/np.pi,'r.')
        #plt.draw()
        #time.sleep(1)
        #plt.show()

    def motion_angle(self,ang,sec):
        print ang," ",
        ang=int(ang)%360
        if(ang in range (0,91)):
            ang=float(ang*np.pi/180)
            v2=-10.0
            v1=(v2)*(np.cos(np.pi/6)-np.tan(ang)-(np.sin(np.pi/6)*np.tan(ang)))
            v1/=(np.tan(ang)+(np.sin(np.pi/6)*np.tan(ang))+np.cos(np.pi/6))
        elif (ang in range (91,181)):
            ang=float(ang*np.pi/180)
            v1=10.0
            v2=(v1)*(np.tan(ang)+(np.sin(np.pi/6)*np.tan(ang))+np.cos(np.pi/6))
            v2/=(np.cos(np.pi/6)-np.tan(ang)-(np.sin(np.pi/6)*np.tan(ang)))
        elif (ang in range (180,270)):
            ang=float(ang*np.pi/180)
            v2=10.0
            v1=(v2)*(np.cos(np.pi/6)-np.tan(ang)-(np.sin(np.pi/6)*np.tan(ang)))
            v1/=(np.tan(ang)+(np.sin(np.pi/6)*np.tan(ang))+np.cos(np.pi/6))
        elif (ang in range (270,360)):
            ang=float(ang*np.pi/180)
            v1=-10.0
            v2=(v1)*(np.tan(ang)+(np.sin(np.pi/6)*np.tan(ang))+np.cos(np.pi/6))
            v2/=(np.cos(np.pi/6)-np.tan(ang)-(np.sin(np.pi/6)*np.tan(ang)))

        v3=-v1-v2
        print v1," ",v2," ",v3
        self.loco(v1,v2,v3,sec)

    def coord_track(self,wx,wy):
        rx=100
        ry=100
        while(abs(rx)>0.5 and abs(ry)>0.5):
            rx=wx-self.x+0.0000000000001
            ry=wy-self.y
            if(ry==0 and rx<0):
                ang=np.pi
            else:
                ang=np.arctan(ry/rx)
            if(ry<0 and rx<0):
                ang+=np.pi
            elif(rx<0):
                ang=np.pi+ang

            ang=ang*180/np.pi
            self.motion_angle(ang,0.01)
            plt.draw()
        
bot=encoder(0,0,0)
# bot.coord_track(5,5)
# bot.coord_track(-5,6)
# bot.coord_track(-6,-5)
# bot.coord_track(4,-4)
plt.ioff()
time.sleep(1)
plt.show()
