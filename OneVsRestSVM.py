from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from DataModel import DataModel

def main():
    data_model = DataModel()
    clf = OneVsRestClassifier(LinearSVC(random_state=0))
    clf.fit(data_model.train_X, data_model.train_y)
    print clf.score(data_model.test_X, data_model.test_y)

if __name__ == '__main__':
    main()
