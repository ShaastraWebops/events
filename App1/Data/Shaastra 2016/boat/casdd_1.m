clc
clear all
num_fil=21;
st_fil=1;

for i=1:num_fil    
    f.(strcat('f',num2str(i)))=xlsread(strcat(num2str(i),'.xlsx'));    
end