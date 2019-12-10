import numpy as np
import csv
import matplotlib.pyplot as plt


def Pima_CSV():
    fp = open('pima.txt','r')
    data = csv.reader(fp,delimiter=',')
    x = []

    for i in data:
        x.append(i[:8])

    fp.close()

    ######################################
    y = []
    fp = open('pima.txt','r')
    data = csv.reader(fp,delimiter=',')

    for i in data:
        y.append(i[-1:])

    fp.close()
    y = np.array(y)

    return x,y


def parse():
    a,b = Pima_CSV()

    X = np.array(a)
    X = X.astype(float)

    Y = np.array(b)
    Y = Y.astype(float)

    m = X.shape[0]
    n = X.shape[1]
    q = (m,1)

    X_ones = np.concatenate((np.ones((m, 1)), X), axis=1)

    return X_ones,Y,X


def star(Var_trans,Var):
    star = Var_trans.dot(Var)
    return star


def main():
    X_ones,Y,X= parse()
    b = Y

    A_star = star(X_ones.T,X_ones)
    A_star_inverse = np.linalg.inv(A_star)

    B_star = star(X_ones.T,b)
    X_star = A_star_inverse.dot(B_star)

    y_hat = np.zeros((Y.shape[0],1))

    for i in range(768):
        count = 0
        for j in range(8):
            count = count + sum(X_star[j+1]*X[i][j])
        y_hat[i] = (count + X_star[0])

    error = np.absolute(np.array(Y)- np.array(y_hat))
    print(error)

    plt.plot(X,Y,'g+',error,'ro')
    plt.show()


if __name__ == '__main__':
    main()
