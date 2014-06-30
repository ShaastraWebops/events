clearvars file;
rows=find(ismember(data(:,19),'') & ismember(data(:,14),{'Submitted'}));

si=size(rows);

t_s=4;
step=t_s+1;

for i = 1:(si(1))
    file(i,1)=num2cell(i);

    file(i,2)=data(rows(i),2);
                    
    file(i,3)=data(rows(i),12);
    
    file(i,4:3+t_s)=data(rows(i),(6+1):(6+t_s));    
            
end

xlswrite('final.xlsx',file)
