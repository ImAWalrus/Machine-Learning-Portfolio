clc;
clear;

test = load('norm_hep_data.dat');
x0 = test(:,1:19);

% loaded up data
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
y = test(:,20);

% rows
m = size(x1,1);
%create augmented x matrix
x = [ones(m,1) x1 x2  x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15 x16 x17 x18 x19];

% Parameters we want to solve fr.
parameters = [0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0;]; 


% Hyper parameters
learningRate = 0.01; %eta
repetition = 500; %epochs

% Storage
costHistory = zeros(repetition,1);

% Iterate across epochs/repetitions
for i = 1:repetition
    % Getting trans of func. inputs
    h = (x*parameters - y)';
    for k = 1:20
    
      % update param.
      parameters(k) = parameters(k) - learningRate * (1/m)*h*x(:,k);
    end
    % Cost func.
    costHistory(i) = (x*parameters - y)' * (x*parameters - y)/(2*m);
    costHistory(i);
end    
plot(costHistory,1:repetition,'b');
%plot(x0,y,'ro',x0,x*parameters,'bo');

%Y(Actual) X*paramters(Prediction)
accuracy = prediction(y,(x*parameters))
write2file(accuracy);
