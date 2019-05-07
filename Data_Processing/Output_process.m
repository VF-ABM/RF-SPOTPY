    
k=1;
for num=1:5400
       
    filename=strcat('C:\Users\AMAN GARG\Desktop\New_5000\Outputs\For all days\Output_Biomarkers_',string(num),'.csv');
    
    if exist(filename, 'file') == 0
        rest(k) = num;
        k=k+1;
        continue;
    end
    %if ~isempty(par)
    par = xlsread(filename);
    out_day0_random(num, :)= par(1,:);
    out_day1_random(num, :)= par(49,:);
    out_day2_random(num, :)= par(97,:);
    out_day3_random(num, :)= par(145,:);
    out_day5_random(num, :)= par(241,:);
    out_day7_random(num, :)= par(337,:);
    out_day14_random(num, :)= par(673,:);
    out_day28_random(num,:) = par(1345,:);
    %end
end
