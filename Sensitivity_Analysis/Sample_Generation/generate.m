
for num=1:5400
    fname = sprintf('sample%d.txt', num);
    fileID = fopen(fname,'w');
    formatSpec = '%.2f\t';

    fprintf(fileID,formatSpec,j(num,:));
    fclose(fileID);
end

