fi=fopen('body_plan_casdd_3.txt','w+');
fprintf(fi,'CUR ');
fprintf(fi,'XYZ * ');   
for j=st_fil:num_fil
    %fi=fopen(strcat('f',num2str(j),'.scr'),'w+');    
    va=f.(strcat('f',num2str(j)));                           
    fprintf(fi,'(%i %i %i) ',va(1,1),va(1,2),va(1,3));        
    %fclose(fi);
end
fclose(fi);
