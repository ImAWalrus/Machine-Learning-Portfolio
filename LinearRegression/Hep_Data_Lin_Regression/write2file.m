function write2file(accuracy)
    fileID = fopen('Lin_Reg_Grad_Desc.dat','w');
    fprintf(fileID,'%f',accuracy);
    fclose(fileID);
    end