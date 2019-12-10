clc;
clear;

% Loaded up data
test = load('norm_hep_data.dat');

x1 = test(:,1).^2; %Alive or Dead
x2 = 2.*test(:,1).*test(:,5); %AntiVirals
x3 = test(:,15).^2; %BILIRUBIN

y = test(:,20);

% Rows
m = size(x1,1);


% Create augmented x matrix
x = [ones(m,1) x1 x2 x3];
n = size(x,2);

% Parameters we want to solve for
parameters = [0; 0 ;0 ;0]; 

% Hyper-Parameters
learningRate = 0.1;%eta
repetition = 10000;%epochs

% Storage
costHistory = zeros(repetition,1);

% Iterate accross epochs/repetitions
for i=1:repetition
    
    % Getting transpose of function inputs
    h = (x*parameters - y)';

    % Update parameters
    for k=1:n
      parameters(k) = parameters(k) - learningRate*(1/m)*h*x(:,k);
    end
    
    % Cost Function
    costHistory(i) = (x*parameters - y)' * (x*parameters - y) / (2*m); 
    costHistory(i);

end
% Plotting our linear fit
#{
figure;
plot3(test(:,1),test(:,2),parameters(1) ...
                        + parameters(2)*x(:,2) ...
                        + 2.*parameters(3)*x(:,3) ...
                        +parameters(4)*x(:,4),'k+');
hold on;
%Pseudo-inverse
x_hat = x'*x;
x_hat_inv = inv(x_hat);
b_hat = x'*y;
theta = x_hat_inv*b_hat
plot(x1,y,'r',x1,x*parameters,'b');
plot3(test(:,1),test(:,2),theta(1) ...
                        + theta(2)*x(:,2) ...
                        + 2.*theta(3)*x(:,3) ...
                        +theta(4)*x(:,4),'b+');

% Plot our cost

figure;
#}
plot(costHistory,1:repetition,'b');


accuracy = prediction(y,(x*parameters))
write2file(accuracy);

