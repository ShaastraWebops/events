function serial_simulate2()

    arena

    %axis([-1000*cos(pi/4) 6000 -1000*cos(pi/4) 6000])

    line(3000+1600*cos(0:0.01:2*pi),3000+1600*sin(0:0.01:2*pi),'color','black')
    line([3000-2670*cos45,3000+2670*cos45],[3000+2670*cos45,3000-2670*cos45],'color','black')
    line(3000+870*cos(0:0.01:2*pi),3000+870*sin(0:0.01:2*pi),'color','black')
    line(3000+870*cos(pi/4)+800*cos(0:0.01:2*pi),3000-870*cos(pi/4)+800*sin(0:0.01:2*pi),'color','black')
            
    a = serial_initialise();
    
    while(1)        
        if(a.BytesAvailable)       
            in=str2num(fscanf(a));
            place(in,500,0);        
        end
    end
%     for i=1:50:12000    
%         place(i,i,0)       
%     end
%     place(i,i,0,1)       
end

function b = serial_initialise()
    %b=serial('COM20','BAUD',115200);
    b=instrfind;    
    si=size(b);   
    fclose(b(si(2)));           
    
    b=serial('COM20','BAUD',115200);
    fopen(b);
    flushinput(b)
end
    
function place(x,y,t,~)
                
    r1=380;
    r2=380;
    r3=380;
    r4=380;
    
    r5=500;          
    
    bcol=[1,1,1];
    l1=line([x,x+r1*cos(t)],[y,y+r1*sin(t)],'color',[0.6,0.6,0.6]);
    l2=line([x,x-r2*sin(t)],[y,y+r2*cos(t)],'color',bcol);
    l3=line([x,x-r3*cos(t)],[y,y-r3*sin(t)],'color',bcol);
    l4=line([x,x+r4*sin(t)],[y,y-r4*cos(t)],'color',bcol);
    l5=line([x,x+r5*cos(t+pi/4)],[y,y+r5*sin(t+pi/4)],'color',bcol);

    plot(x,y,'color',bcol);
    
    drawnow
    
    pause(0.040)
    if(nargin==3)
        delete(l1,l2,l3,l4,l5);
    end
    
    drawnow
end