#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics


def plant_classification():
    # Download the Iris dataset
    data = load_iris()
    X, y = data.data, data.target

    # Get the training and test datasets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=0)
    print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

    # Gaussian Naive Bayes
    model = naive_bayes.GaussianNB()

    # Train the model on the training data
    model.fit(X_train, y_train)

    # Predict y-values with the trained model on the test data
    y_fitted = model.predict(X_test)

    # Get the accuracy of the model
    acc = metrics.accuracy_score(y_fitted, y_test)

    return acc


def main():
    print(f"Accuracy is {plant_classification()}")


if __name__ == "__main__":
    main()
