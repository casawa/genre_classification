from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from DataModel import DataModel

def main():
    print "Loading data..."
    data_model = DataModel()
    clf = OneVsRestClassifier(LinearSVC(random_state=0))
    print "Training classifier..."
    clf.fit(data_model.train_X, data_model.train_y)
    print "Evaluating classifier..."
    print "Average Test Accuracy", clf.score(data_model.test_X, data_model.test_y)

if __name__ == '__main__':
    main()
