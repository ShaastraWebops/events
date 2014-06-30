r_z=[0,500,1000,1500,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000];

fi=fopen('half_breadth.scr','w+');

for i=r_z
    fprintf(fi,'spline\r\n');
    for j=st_fil:num_fil
        cur_fil=f.(strcat('f',num2str(j)));
        index=find(cur_fil(:,3)==i);
        if(index)
            fprintf(fi,'%i,%i,%i\r\n',cur_fil(index,1),cur_fil(index,2),cur_fil(index,3));
        end
    end
    fprintf(fi,'\r\n\r\n\r\n\r\n\r\n\r\n\r\n');    
end
        
fclose(fi);
