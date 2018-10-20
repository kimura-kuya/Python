from sklearn import svm,datasets

iris = datasets.load_iris()

bunrui = svm.SVC(C=1.0,kernel='linear')
bunrui.fit(iris.data,iris.target)
print(iris.target)
yosoku = bunrui.predict(iris.data)
print(yosoku)