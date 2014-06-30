clc
clear all
st_fil=0;
num_fil=20;

for i=st_fil:num_fil    
    f.(strcat('f',num2str(i)))=xlsread(strcat(num2str(i),'.xlsx'));    
end

for i=st_fil:num_fil
    f.(strcat('f',num2str(i)))=round(1000*f.(strcat('f',num2str(i))));
end