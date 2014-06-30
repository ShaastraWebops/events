arena

%axis([-1000*cos(pi/4) 6000 -1000*cos(pi/4) 6000])

line(3000+1600*cos(0:0.01:2*pi),3000+1600*sin(0:0.01:2*pi),'color','black')
line([3000-2670*cos45,3000+2670*cos45],[3000+2670*cos45,3000-2670*cos45],'color','black')
line(3000+870*cos(0:0.01:2*pi),3000+870*sin(0:0.01:2*pi),'color','black')
line(3000+870*cos(pi/4)+800*cos(0:0.01:2*pi),3000-870*cos(pi/4)+800*sin(0:0.01:2*pi),'color','black')
