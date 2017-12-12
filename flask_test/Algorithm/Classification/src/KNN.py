from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn import model_selection, cross_validation

def get_KNN(n_neighbors=5, algorithm='auto', random_state=100, test_size=0.2):
    '''

    :param n_neighbors:
    :param algorithm:
    :param random_state:
    :param test_size:
    :return:
    '''
    iris = load_iris()
    X = iris.data
    Y = iris.target

    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=random_state)
    DT = KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=algorithm).fit(X_train, Y_train)
    return DT.score(X_test, Y_test)

if __name__ == '__main__':
    get_KNN()