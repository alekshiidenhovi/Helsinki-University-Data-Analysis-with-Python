#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet = "abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words


def load_finnish():
    finnish_url = "https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename = "src/kotus-sanalista_v1.xml"
    load_from_net = False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines = []
            for line in data:
                lines.append(line.decode('utf-8'))
        doc = "".join(lines)
    else:
        with open(filename, "rb") as data:
            doc = data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))


def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines = map(lambda s: s.rstrip(), data.readlines())
    return lines


def get_features(a):
    # # Zip alphabets and their respective indices
    # def get_alphabet():
    #     return dict(zip(list("abcdefghijklmnopqrstuvwxyzäö-"), np.zeros((29,)).astype(int)))

    # # Frequencies of the letters in words
    # freqs = np.array([])

    # # Loop over letters and get their frequencies
    # for word in a:
    #     alphabet = get_alphabet()
    #     for letter in word:
    #         alphabet[letter] += 1

    #     values = np.array(list(alphabet.values()))
    #     values = values.reshape(1, len(values))
    #     # length = len(vals)
    #     # vals = np.reshape(vals, (1, length))

    #     if len(freqs) == 0:
    #         freqs = np.array(values)
    #     else:
    #         freqs = np.concatenate([freqs, values])

    # # Return the letter frequency array
    # return freqs

    alphabets = list("abcdefghijklmnopqrstuvwxyzäö-")
    array = []
    for word in a:
        histogram = np.zeros(29,)
        for letter in word:
            n = 0
            while n < 29:
                if letter == alphabets[n]:
                    histogram[n] += 1
                    break
                n = n+1

        array.append(histogram)

    return np.array(array)


def contains_valid_chars(s):
    alphabet = list("abcdefghijklmnopqrstuvwxyzäö-")
    return all([char in alphabet for char in s])


def get_features_and_labels():
    # Load the datasets
    fin = load_finnish()
    eng = load_english()

    # Helper function to filter the lists
    def filtering(lst):
        return np.array(list(filter(contains_valid_chars, map(lambda word: word.lower(), lst))))

    # Filter finnish and english lists
    fin = filtering(fin)
    eng = filtering(
        np.array(list(filter(lambda word: not word[0].isupper(), eng))))

    # Get the feature matrices
    fin_feat = get_features(fin)
    eng_feat = get_features(eng)
    features = np.concatenate((fin_feat, eng_feat))

    # Get the target values
    target = np.concatenate((np.zeros(len(fin_feat)), np.ones(len(eng_feat))))

    return features, target


def word_classification():
    # Get features and labels
    X, y = get_features_and_labels()

    # Use multinomial Naive Bayes as the model
    model = MultinomialNB()

    # Print the k-fold score
    print(cross_val_score(model, X, y, cv=5))

    # Return the cv-scores
    return cross_val_score(model, X, y, cv=model_selection.KFold(
        n_splits=5, shuffle=True, random_state=0))


def main():
    print("Accuracy scores are:", word_classification())


if __name__ == "__main__":
    main()
