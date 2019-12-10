clc
clear

x = load('x_data.dat')'; 
y = load('y_data.dat')'; 
z = load('z_data.dat')';

N_x = size(x);

x0 = ones(N_x(1),1); 


A = [x y x0]
b = z;
     
A_trans = A';

A_star = A_trans*A;

B_star = A_trans*b;

A_cross = inv(A_star);

X_star = A_cross*B_star;

m1_star = X_star(1);
m2_star = X_star(2);
b_star = X_star(3);

z_star = m1_star*x + m2_star*y +b_star
error = abs(z-z_star)


plot3(x,y,z,'g+',x,y,z_star,'r+') 