clearvars file;
j=1;
for i=2:size(data(:,1))
    if(~isempty(data{i,1}))
        for k=0:4            
            if(~isempty(data{i,3+k}))
                file(j,1)=data(i,3+k);
                file(j,2)=data(i+2,3+k);
                file(j,3)=data(i,8+k);
                j=j+1;
            end
        end        
    end
end


xlswrite('final.xlsx',file)
