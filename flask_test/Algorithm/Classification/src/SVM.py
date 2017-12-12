from sklearn import svm
from sklearn.datasets import load_iris
from sklearn import model_selection, cross_validation

def get_svm(C=1.0, kernel='rbf', max_iter=1, gamma='auto', random_state=100, test_size=0.2):
    '''

    :param C: penalty factor
    :param kernel: 'linear', 'rbf', 'poly', 'sigmoid'
    :param max_iter: max iters
    :param gamma:
    :param random_state: random state
    :param size: split train and test
    :return: score of prediction
    '''
    iris = load_iris()
    X = iris.data
    Y = iris.target

    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=random_state)
    svc = svm.SVC(kernel=kernel, C=C, max_iter=max_iter, gamma=gamma).fit(X_train,Y_train)
    return svc.score(X_test, Y_test)



