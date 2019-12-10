clc;
clear;

% Loaded up data
test = load('norm_hep_data.dat');

x1 = test(:,1);
x2 = test(:,2);
x3 = test(:,3);
x4 = test(:,4);
x5 = test(:,5);
x6 = test(:,6);
x7 = test(:,7);
x8 = test(:,8);
x9 = test(:,9);
x10 = test(:,10);
x11 = test(:,11);
x12 = test(:,12);
x13 = test(:,13);
x14 = test(:,14);
x15 = test(:,15);
x16 = test(:,16);
x17 = test(:,17);
x18 = test(:,18);
x19 = test(:,19);
y  = test(:,20);

% Rows
m = size(x1,1);

% Create augmented x matrix
x = [ones(m,1) x1 x2  x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15 x16 x17 x18 x19];
n = size(x,2);
m = size(x1,1);
n = size(x,2);


% Parameters we want to solve for
parameters = [0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; ]; 

% Hyper-Parameters
learningRate = 0.01;%eta
repetition = 20000;%epochs

% Storage
costHistory = zeros(repetition,1);

% Iterate accross epochs/repetitions
for i=1:repetition
    
    % Getting transpose of function inputs
    y_hat = sigmoid(x*parameters);
    h = (y_hat - y)';

    % Update parameters
    for k=1:n
      parameters(k) = parameters(k) - learningRate*(1/m)*h*x(:,k);
    end
        
    % Cost Function
    sum_cost = 0;
    for j=1:n
        sum_cost = sum_cost + (y(j)*log(y_hat(j))+(1-y(j))*log(1-y_hat(j)));
    end
    costHistory(i) = -sum_cost;

end

% Plot our cost
plot(1:repetition,costHistory,'b');
accuracy = prediction(y,y_hat);
write2file(accuracy);