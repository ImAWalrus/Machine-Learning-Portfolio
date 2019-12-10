import numpy as np
import csv
import matplotlib.pyplot as plt
from math import sqrt


def Pima_CSV():
    fp = open('pima.txt','r')
    data = csv.reader(fp,delimiter=',')
    x = []

    for i in data:
        x.append(i[:8])

    fp.close()

    return x


def gen_data():
    a = Pima_CSV()
    X = np.array(a)
    X = X.astype(float)

    return X

def gen_centroid(X):
    m = X.shape[0]
    n = X.shape[1]
    K = 2
    centroids = np.zeros(K)
    rand_idx = np.random.permutation(m)
    centroids = X[rand_idx[0:K],:]

    return centroids,K


def eucl_dist(X,centroids,K):
    m = X.shape[0]
    n = X.shape[1]
    q = (m,1)
    indices = np.zeros(q)
    bin0 = []
    bin1 = []


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


    bin0 = np.asarray(bin0)
    bin1 = np.asarray(bin1)

    return bin0,bin1

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
    X = X[:,[1,2]] #(768,2)
    X_0 = X[:384]
    X_1 = X[384:768]

    print(X)
    cent,K = gen_centroid(X)

    plt.plot(X_0[:,0],X_0[:,1],'b*',X_1[:,0],X_1[:,1],'r*')
    plt.plot(cent[:,0],cent[:,1],'ko')
    plt.show()



    bin0,bin1 = eucl_dist(X,cent,K)

    print(bin0.shape,bin1.shape)
    new_cent = cent

    for i in range(10):
        bin0,bin1 = eucl_dist(X,new_cent,K)
        c1 = new_centroid(bin0)
        c2 = new_centroid(bin1)
        new_cent = np.vstack([c1,c2])
        print("\nIteration {} | New Centroids {}\n".format(i,new_cent))

    plt.plot(X_0[:,0],X_0[:,1],'b*',X_1[:,0],X_1[:,1],'r*')
    plt.plot(new_cent[:,0],new_cent[:,1],'ko')
    plt.show()


if __name__ == '__main__':
    main()
