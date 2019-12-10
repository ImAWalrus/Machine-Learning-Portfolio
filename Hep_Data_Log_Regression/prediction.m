function a = prediction(y,y_hat)
    
    correct = 0;
    [n m] = size(y);
    for i=1:n
        if((y_hat(i) >= 0.50) && y(i) == 1)
            correct = correct + 1;
        elseif((y_hat(i) < 0.50) && y(i) == 0)
            correct = correct + 1;
        end
                
    correct
    a = correct / n * 100;
    end       
     
 end