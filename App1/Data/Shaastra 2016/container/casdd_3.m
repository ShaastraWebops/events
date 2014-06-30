r_y=[0,1500,3000,6000,9000,12000,15000];

fi=fopen('profile.scr','w+');

for i=r_y
    fprintf(fi,'spline\r\n');
    for j=st_fil:num_fil
        cur_fil=f.(strcat('f',num2str(j)));
        index=find(cur_fil(:,2)==i);
        if(index)
            fprintf(fi,'%i,%i,%i\r\n',cur_fil(index,1),cur_fil(index,2),cur_fil(index,3));
        end
    end
    fprintf(fi,'\r\n\r\n\r\n\r\n\r\n\r\n\r\n');    
end
        
fclose(fi);
