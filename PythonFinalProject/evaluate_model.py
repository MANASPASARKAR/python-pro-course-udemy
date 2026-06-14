from sklearn.metrics import classification_report, confusion_matrix

class EvaluateModel:

    def evaluation(self, y_test, pred):

        print(classification_report(y_test, pred))
        print("\n")
        print(confusion_matrix(y_test, pred))
