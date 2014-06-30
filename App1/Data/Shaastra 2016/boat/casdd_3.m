r_y=[500,1000,2000,3000,4000,5000];

fi=fopen('profile.scr','w+');

for i=r_y
    fprintf(fi,'spline\r\n');
    for j=1:num_fil
        cur_fil=f.(strcat('f',num2str(j)));
        index=find(cur_fil(:,2)==i);
        if(index)
            fprintf(fi,'%i,%i,%i\r\n',cur_fil(index,1),cur_fil(index,2),cur_fil(index,3));
        end
    end
    fprintf(fi,'\r\n\r\n\r\n\r\n\r\n\r\n\r\n');    
end
        
fclose(fi);
