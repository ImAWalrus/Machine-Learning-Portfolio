import numpy as np
import csv
import matplotlib.pyplot as plt
from math import sqrt


def iris_CSV():
    fp = open('iris_data.dat','r')
    data = csv.reader(fp,delimiter=',')
    x = []

    for i in data:
        x.append(i[:4])

    fp.close()

    return x


def gen_data():
    a= iris_CSV()
    X = np.array(a)
    X = X.astype(float)

    return X


def gen_centroid(X):
    m = X.shape[0]
    n = X.shape[1]
    K = 3
    centroids = np.zeros(K)
    rand_idx = np.random.permutation(m)
    centroids = X[rand_idx[0:K],:]

    print(centroids.shape)

X = gen_data()
gen_centroid(X)
    return centroids,K


def eucl_dist(X,centroids,K):
    m = X.shape[0]
    n = X.shape[1]
    q = (m,1)
    indices = np.zeros(q)

    bin0 = []
    bin1 = []
    bin2 = []


    for i in range(m):
        k = 1
        min_distance = sqrt(sum((X[i,:]-centroids[1,:]))**2)
        j=1
        for j in range(K):
            distance = sqrt(sum((X[i,:]-centroids[j,:]))**2)
            if(distance < min_distance):
                min_distance = distance
                k = j

        indices[i] = k
    test = np.concatenate((X,indices), axis=1)

    for i in test:
        for j in i:
            if(j == 0.):
                bin0.append(i[:2])
            elif(j == 1.):
                bin1.append(i[:2])
            elif(j == 2.):
                bin2.append(i[:2])

    bin0 = np.asarray(bin0)
    bin1 = np.asarray(bin1)
    bin2 = np.asarray(bin2)

    return bin0,bin1,bin2


def new_centroid(array):
    sum_x = 0
    sum_y = 0

    b = len(array)

    if(b == 0):
        return sum_x,sum_y
    else:
        for i in range(b):
            sum_x = sum_x + array[i][0]
            sum_y = sum_y + array[i][1]

        sum_x = sum_x / b
        sum_y = sum_y / b

        return sum_x,sum_y


def main():
    X = gen_data()
    print(X.shape)

    X = X[:,[2,3]]
    X_0 = X[:50]
    X_1 = X[50:100]
    X_2 = X[100:150]

    cent,K = gen_centroid(X)

    plt.plot(X_0[:,0],X_0[:,1],'r*',X_1[:,0],X_1[:,1],'b*',X_2[:,0],X_2[:,1],'g*')
    plt.plot(cent[:,0],cent[:,1],'ko',label='Centroids')
    plt.xlabel('Petal Length')
    plt.ylabel('Petal Width')
    plt.legend()
    plt.show()


    bin0,bin1,bin2 = eucl_dist(X,cent,K)

    print(bin0.shape,bin1.shape,bin2.shape)
    new_cent = cent

    for i in range(10):
        bin0,bin1,bin2 = eucl_dist(X,new_cent,K)
        c1 = new_centroid(bin0)
        c2 = new_centroid(bin1)
        c3 = new_centroid(bin2)
        new_cent = np.vstack([c1,c2,c3])
        print("\nIteration {} | New Centroids {}\n".format(i,new_cent))

    plt.plot(X_0[:,0],X_0[:,1],'r*',X_1[:,0],X_1[:,1],'b*',X_2[:,0],X_2[:,1],'g*')
    plt.plot(new_cent[:,0],new_cent[:,1],'mo',label='Centroids')
    plt.xlabel('Petal Length')
    plt.ylabel('Petal Width')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
