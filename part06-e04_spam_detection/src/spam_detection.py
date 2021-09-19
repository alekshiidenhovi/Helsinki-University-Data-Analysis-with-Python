#!/usr/bin/env python3

import numpy as np
from gzip import open
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


def spam_detection(random_state=0, fraction=1.0):
    # Read lines from the files
    with open("src/ham.txt.gz") as f:
        ham = f.readlines()
    with open("src/spam.txt.gz") as g:
        spam = g.readlines()

    # Take the fraction of the lines
    ham = np.array(ham)[:round(fraction * len(ham))]
    spam = np.array(spam)[:round(fraction * len(spam))]

    # All the emails
    emails = np.concatenate((ham, spam))

    # Labels
    zeros = np.zeros(len(ham))
    ones = np.ones(len(spam))
    y = np.concatenate((zeros, ones))

    # Create the vectorizer and the feature matrix
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(emails)

    # Divide the feature matrices and labels to training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=random_state)

    # Multinomial naive bayes model
    model = MultinomialNB()

    # Train the model with the training data
    model.fit(X_train, y_train)

    # Predict y-labels for the test set
    y_predict = model.predict(X_test)

    # Get the accuracy of the predictions
    acc = accuracy_score(y_test, y_predict)

    # Return the accuracy, size of the test set and number of misclassified sample points
    return acc, len(y_test), int((1 - acc) * len(y_test))


def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")


if __name__ == "__main__":
    main()
