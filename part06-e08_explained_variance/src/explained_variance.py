#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA


def explained_variance():
    # Read the tsv-file into a dataframe
    df = pd.read_csv("src/data.tsv", sep="\t")

    # Initialize PCA-model
    model = PCA(10)

    # Fit the data in the model
    model.fit(df)

    # Return variance and explained variance
    return list(df.var()), list(model.explained_variance_)


def main():
    v, ev = explained_variance()
    # print(sum(v), sum(ev))

    print("The variances are: ", end="")
    for var in v:
        # for val in arr:
        print(f"{var:.3f}", end=" ")

    print("\n")

    print(f"The explained variances after PCA are: ", end="")
    for explained_var in ev:
        print(f"{explained_var:.3f}", end=" ")

    # Plot the cumulative explained variance
    plt.plot(np.arange(1, 11), np.cumsum(ev))
    plt.show()


if __name__ == "__main__":
    main()
