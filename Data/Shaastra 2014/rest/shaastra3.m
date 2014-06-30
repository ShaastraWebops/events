clearvars file;
rows=find(ismember(data(:,21),'Yes'));

si=size(rows);

t_s=5;
step=t_s+1;

for i = 1:(si(1))
    file(i,1)=num2cell(i);

    file(i,2)=data(rows(i),2);
                    
    file(i,3)=data(rows(i),15);
    
    file(i,4:3+t_s)=data(rows(i),(7+1):(7+t_s));    
            
end

xlswrite('final.xlsx',file)
