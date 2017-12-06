import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import svm
from sklearn.datasets import load_iris

# 可视化
iris = load_iris()
X = iris.data[:,:2]
Y = iris.target
C = 1.0
svc = svm.SVC(kernel='linear', C=C).fit(X,Y)
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X,Y)
poly_sv = svm.SVC(kernel='poly', degree=3, C=C).fit(X,Y)
lin_svc = svm.LinearSVC(C=C).fit(X,Y)

h = 0.02
# get grid
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
# get title
titles = ['SVC with linear kernel',
          'SVC with RBF kernel',
          'SVC with Polynomial kernel',
          'Linear SVC']

for i,clf in enumerate((svc,rbf_svc,poly_svc,lin_svc)):
    plt.subplot(2,2,i+1)
    plt.subplots_adjust(wspace=0.3, hspace=0.3)

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.2)

    plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i])

plt.show()