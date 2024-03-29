import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
digits = datasets.load_digits()

clf = svm.SVC(gamma=0.0001, C=100) 

x,y = digits.data[:-10], digits.target[:-10]
clf.fit(x,y)

print("Prediction:",clf.predict(digits.data[[-9]]))
plt.imshow(digits.images[-9], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()
