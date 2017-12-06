
def train_test_(X, Y, test_size = 0.2, random_state = 100):
    from sklearn.cross_validation import train_test_split
    # input : test_size, random_state
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=test_size,random_state=random_state)
    return X_train, X_test, Y_train, Y_test

