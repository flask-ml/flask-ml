from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.datasets import load_iris
from sklearn import model_selection, cross_validation

def get_NB(kernel='GaussianNB', random_state=100, test_size=0.2):
    iris = load_iris()
    X = iris.data
    Y = iris.target

    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=random_state)
    if kernel == 'GaussianNB':
        GNB = GaussianNB().fit(X_train, Y_train)
        return GNB.score(X_test, Y_test)
    elif kernel == 'MultinomialNB':
        MNB = MultinomialNB().fit(X_train, Y_train)
        return MNB.score(X_test, Y_test)
    elif kernel == 'BernoulliNB':
        BNB = BernoulliNB().fit(X_train, Y_train)
        return BNB.score(X_test, Y_test)

if __name__ == '__main__':
    get_NB()