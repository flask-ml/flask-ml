from sklearn import tree
from sklearn.datasets import load_iris
from sklearn import model_selection, cross_validation

def get_DecisionTree(criterion='gini', min_samples_split=2, max_features=None, random_state=100, test_size=0.2):
    '''

    :param criterion:  The function to measure the quality of a split.
    :param min_sample_split: The minimum number of samples required to split an internal node:
                             (1)If int, then consider min_samples_split as the minimum number.
                             (2)If float, then min_samples_split is a percentage and ceil(min_samples_split * n_samples) are the minimum number of samples for each split.
    :param max_feature: The number of features to consider when looking for the best split.
    :param random_state: random state
    :param size: split train and test
    :return: score of prediction
    '''
    iris = load_iris()
    X = iris.data
    Y = iris.target

    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=random_state)
    DT = tree.DecisionTreeClassifier(criterion=criterion, min_samples_split=min_samples_split, max_features=max_features).fit(X_train, Y_train)
    return DT.score(X_test, Y_test)

if __name__ == '__main__':
    get_DecisionTree()

