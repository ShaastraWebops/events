fi=fopen('body_plan_casdd.txt','w+');

for j=st_fil:num_fil
    %fi=fopen(strcat('f',num2str(j),'.scr'),'w+');
    fprintf(fi,'CUR ');
    va=f.(strcat('f',num2str(j)));    
    fprintf(fi,'stn%i\r\n',va(1,1));    
    fprintf(fi,'X %i\r\n',va(1,1));
    fprintf(fi,'YZ * ');   
    i=0;
    for i=1:size(va(:,1))        
        fprintf(fi,'(%i %i) ',va(i,2),va(i,3));
        i=i+1;
        if(i==10)
            fprintf(fi,',\r\n');
            i=0;
        end        
    end
    fprintf(fi,'\r\n\r\n');    
    %fclose(fi);
end
fclose(fi);
