close all;
clear all;

par = xlsread('parameters.xlsx','sheet1'); # location of parameter specifications (number, mean, SD, range, and type*)
size=5400;
for i=1:213
    stats(i,1) = i;
    a = par(i,4);
    b = par(i,5);
    
    % For lognormal distibution (*Type 1)
    if par(i,6)==1
        r = (b-a).*rand(size,1) + a; 
        j(:,i)=r;
        histfit(r);
        skewness(r);
        stats(i,2) = mean(log(r));
        stats(i,3) = std(log(r));
        
    % For discrete lognormal distibution (*Type 2)
	elseif par(i,6)==2        
        x = (b-a).*rand(size,1) + a; 
        y=floor(x);
        for p=1:size
            if x(p)-y(p) >= 0.5
                r(p) = y(p) + 0.5;
            else
                r(p) = y(p);
            end
        end
        j(:,i)=r;
        histfit(r);
        skewness(r);
        stats(i,2) = mean(log(r));
        stats(i,3) = std(log(r));     
               
    % For normal distibution (*Type 3, half life)
	elseif par(i,6)==3
        r = (b-a).*rand(size,1) + a; 
        j(:,i)=r;
        histfit(r);
        skewness(r);
        stats(i,2) = mean(r);
        stats(i,3) = std(r);
        
    end 
    stats(i,4) = min(r);
    stats(i,5) = max(r);   
end
