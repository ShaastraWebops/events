clearvars file;
rows=find(ismember(data(:,19),'Yes'));
filter=find(ismember(data(rows,21),'Yes'));
rows=rows(filter);

si=size(rows);

t_s=4;
step=t_s+1;

for i = 1:(si(1)-1)
    file(step*(i-1)+1,1)=num2cell(i);

    file(step*(i-1)+1,2)=data(rows(i),2);
    
    file(step*(i-1)+1:step*(i-1)+t_s,3)=data(rows(i),(23+1):(23+t_s));
    
    file(step*(i-1)+1:step*(i-1)+t_s,4)=data(rows(i),(2+1):(2+t_s));
    
    file(step*(i-1)+1:step*(i-1)+t_s,5)=data(rows(i),(6+1):(6+t_s));
    
    file(step*(i-1)+1:step*(i-1)+t_s,6)=data(rows(i)+1,(6+1):(6+t_s));
    
end

xlswrite('final.xlsx',file)
