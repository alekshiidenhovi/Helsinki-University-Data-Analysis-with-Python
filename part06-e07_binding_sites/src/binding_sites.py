#!/usr/bin/env python3

import scipy.cluster.hierarchy as hc
import scipy.spatial as sp
import pandas as pd
import numpy as np
import scipy
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)


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


def toint(x):
    # Turn the string into a list
    lst = list(x)

    # Helper function to translate the string into a list of numbers
    def translate(letter):
        dictionary = {"A": 0, "C": 1, "G": 2, "T": 3}
        return dictionary[letter]

    # Return the list of numbers
    return list(map(translate, lst)) if len(lst) > 1 else translate(x)


def get_features_and_labels(filename):
    # Get the original dataframe
    df = pd.read_csv(filename, sep="\t")
    X = np.array(list(map(toint, df.X)))
    y = np.array([df.y]).T

    return (X, y)


def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g = sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage)
    g.fig.suptitle(
        f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()


def cluster_euclidean(filename):
    # Get the feature matrix and label vector
    features, labels = get_features_and_labels(filename)

    # Initialize the clustering model
    model = AgglomerativeClustering(
        affinity="euclidean", linkage="average").fit(features)

    # Predicted labels
    y_predicted = model.labels_

    # Find the permutation and get the new labels
    permutation = find_permutation(labels, y_predicted)
    new_labels = [permutation[label] for label in y_predicted]

    return accuracy_score(new_labels, labels)


def cluster_hamming(filename):
    # Get the feature matrix and label vector
    features, labels = get_features_and_labels(filename)

    # Calculate the hamming distance
    hamming_dist = pairwise_distances(features, metric="hamming")

    # Initialize the clustering model
    model = AgglomerativeClustering(
        affinity="precomputed", linkage="average").fit(hamming_dist)

    # Predicted labels
    y_predicted = model.labels_

    # Find the permutation and get the new labels
    permutation = find_permutation(labels, y_predicted)
    new_labels = [permutation[label] for label in y_predicted]

    return accuracy_score(new_labels, labels)


def main():
    print("Accuracy score with Euclidean affinity is",
          cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is",
          cluster_hamming("src/data.seq"))


if __name__ == "__main__":
    main()
