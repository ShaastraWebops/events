function b = serial_init()
    %b=serial('COM20','BAUD',115200);
    b=instrfind;    
    si=size(b);   
    fclose(b(si(2)));           
    
    b=serial('COM20','BAUD',115200);
    %fopen(b);
    %flushinput(b)
    disp('done');
end
