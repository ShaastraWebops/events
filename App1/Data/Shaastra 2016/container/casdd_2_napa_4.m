r_y=[0,1500,3000,6000,9000,12000,15000];

fi=fopen('profile.txt','w+');

for i=r_y
    fprintf(fi,'CUR ');
    fprintf(fi,'f%i\r\n',i);
    fprintf(fi,'XYZ * ');
    for j=st_fil:num_fil
        cur_fil=f.(strcat('f',num2str(j)));
        index=find(cur_fil(:,2)==i);
        k=0;
        if(index)            
            fprintf(fi,'(%i %i %i) ',cur_fil(index,1),cur_fil(index,2),cur_fil(index,3));
            k=k+1;
            if(k==10)
                fprintf(fi,',\r\n');
            end
        end
    end
    fprintf(fi,'\r\n\r\n\r\n\r\n\r\n\r\n\r\n');    
end
        
fclose(fi);
