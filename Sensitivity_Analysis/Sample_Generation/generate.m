for num=1:5400 % number of iterations of sensitivity analysis
    fname = sprintf('sample%d.txt', num); % name of each individual sample text file, used as input for the VF-ABM
    fileID = fopen(fname,'w');
    formatSpec = '%.2f\t';

    fprintf(fileID,formatSpec,j(num,:)); % 'j' is input from 'sample_generate.m'
    fclose(fileID);
end
