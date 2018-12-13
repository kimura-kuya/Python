# -*- coding: utf-8 -*-
"""MLPCiris

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11UU0EGRpjME-OcsvFx_TMICbPBTewlYx
"""

from sklearn.neural_network import MLPClassifier
from sklearn import datasets

iris = datasets.load_iris()


d = iris.data
l = iris.target
clf = MLPClassifier(hidden_layer_sizes=(100,100,100), max_iter=100000, tol=0.0001, random_state=1)
clf.fit(d,l)
r = clf.predict(d)
print(l)
print(r)