fi=fopen('body_plan_casdd.txt','w+');

for j=st_fil:num_fil
    %fi=fopen(strcat('f',num2str(j),'.scr'),'w+');    
    va=f.(strcat('f',num2str(j)));    
    fprintf(fi,'stn%i ',va(1,1));            
    %fclose(fi);
end
fclose(fi);
