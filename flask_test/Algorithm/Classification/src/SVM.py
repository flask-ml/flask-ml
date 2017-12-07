from sklearn import svm
from sklearn.datasets import load_iris
from flask_test.Algorithm.Classification.src.train_test import train_test_

def main(t):
    iris = load_iris()
    X = iris.data
    Y = iris.target
    # input : kernel
    kernel = ['linear', 'rbf', 'poly']
    C = 1.0

    X_train, X_test, Y_train, Y_test = train_test_(X, Y, t, 100)

    svc = svm.SVC(kernel='linear', C=C).fit(X_train,Y_train)
    print("SVC with linear kernel: ",svc.score(X_test,Y_test))
    rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X_train,Y_train)
    print("SVC with RBF kernel: ",rbf_svc.score(X_test,Y_test))
    poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X_train,Y_train)
    print("SVC with Polynomial kernel: ",poly_svc.score(X_test,Y_test))
    lin_svc = svm.LinearSVC(C=C).fit(X_train,Y_train)
    print("Linear SVC: ",lin_svc.score(X_test,Y_test))
    return svc.score(X_test, Y_test)

if __name__ == '__main__':
    main()


