#!/usr/bin/env python3

import pandas as pd
import numpy as np
import scipy
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score


def find_permutation(real_labels, labels):
    permutation = []
    m = max(labels) + 1
    for i in range(m):
        # Initialize np-arrays with no negative labels and real labels
        no_negatives = np.array(labels)
        reals = np.array(real_labels)

        # Get the indices of the labels that are not outliers
        indices = no_negatives != -1

        # Get rid off outliers
        reals = reals[indices]
        no_negatives = no_negatives[indices]

        # Get the true-false values for the labels that match the current label i
        idx = no_negatives == i
        # idx = labels == 1

        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(reals[idx])[0][0]
        # new_label = scipy.stats.mode(real_labels[idx])[0][0]

        # Append the label to the permutation array
        permutation.append(new_label)

    return permutation


def nonconvex_clusters():
    # Dataframe
    df = pd.read_csv("src/data.tsv", sep="\t")
    X = df[["X1", "X2"]]
    y = df.y
    print(X, X.values)

    # Dataframe arrays
    eps = []
    acc_scores = []
    no_clusters = []
    no_outliers = []

    # Loop over eps values and collect results
    for ep in np.arange(0.05, 0.2, 0.05):
        # Initialize model and predict the labels
        model = DBSCAN(eps=ep)
        labels = model.fit_predict(X)

        # Number of labels
        clusters = max(labels) + 1

        # Find the permutation vector and get the new labels
        permutation = find_permutation(y, labels)

        # Get the indices where labels == -1
        idx = labels == -1

        # New labels
        new_labels = [permutation[label] for label in labels[~idx]]

        # Get the accuracy score
        acc = (accuracy_score(y[~idx], new_labels)
               if clusters == 2 else np.nan)

        # Outliers
        outliers = np.sum(idx)

        # Append the values to the arrays
        eps.append(ep)
        acc_scores.append(acc)
        no_clusters.append(clusters)
        no_outliers.append(outliers)

    return pd.DataFrame(list(zip(eps, acc_scores, no_clusters, no_outliers)), columns=["eps", "Score", "Clusters", "Outliers"]).astype(float)


def main():
    print(nonconvex_clusters())


if __name__ == "__main__":
    main()
