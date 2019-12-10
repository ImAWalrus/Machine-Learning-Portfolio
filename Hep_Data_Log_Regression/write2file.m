function write2file(accuracy)
    fileID = fopen('Log_Reg.dat','w');
    fprintf(fileID,'%f',accuracy);
    fclose(fileID);
    end