from xgboost import XGBClassifier
from sklearn.datasets import load_iris
from sklearn import model_selection, cross_validation
from sklearn.metrics import accuracy_score

def get_XGB(gamma=0.2, max_depth=10, learning_rate=0.001, random_state=100, test_size=0.2):
    '''

    :param gamma:
    :param max_depth:
    :param learning_rate:
    :param random_state:
    :param test_size:
    :return:
    '''
    iris = load_iris()
    X = iris.data
    Y = iris.target

    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=random_state)
    XGB = XGBClassifier(base_score=0.5, colsample_bylevel=1, colsample_bytree=0.8,
       gamma=gamma, learning_rate=learning_rate, max_delta_step=5, max_depth=max_depth,
       min_child_weight=0.1, missing=None, n_estimators=100, nthread=3,
       objective='multi:softprob', reg_alpha=0, reg_lambda=1,
       scale_pos_weight=1, seed=0, silent=True, subsample=0.8)

    XGB.fit(X_train, Y_train)
    Y_pred = XGB.predict(X_test)
    # print(accuracy_score(Y_test, Y_pred))
    return accuracy_score(Y_test, Y_pred)

if __name__ == '__main__':
    get_XGB()