filename_in=strcat('C:\Users\AMAN GARG\SA\input_home.xlsx'); % path to input file
par_in = xlsread(filename_in);

for num=1:5400
    flag=0;
    for j=1:2371
        if num == rest(j)
            flag=1;
        end
    end
    
    if flag == 0
        input(num,:) = par_in(num,:) 
    end
end
