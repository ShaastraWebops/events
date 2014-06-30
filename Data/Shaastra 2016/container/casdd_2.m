fi=fopen('body_plan.scr','w+');

for j=st_fil:num_fil
    %fi=fopen(strcat('f',num2str(j),'.scr'),'w+');
    fprintf(fi,'spline\r\n');
    va=f.(strcat('f',num2str(j)));    
    for i=1:size(va(:,1))
        fprintf(fi,'%i,%i,%i\r\n',va(i,1),va(i,2),va(i,3));
    end
    fprintf(fi,'\r\n\r\n\r\n\r\n\r\n\r\n\r\n');    
    %fclose(fi);
end
fclose(fi);
