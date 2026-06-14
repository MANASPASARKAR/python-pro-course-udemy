import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
import joblib
from sklearn.preprocessing import StandardScaler
from cleaner import Cleaner
from visualizer import Visualizer
from train_model import TrainModel
from evaluate_model import EvaluateModel


df = pd.read_csv('cardio_train.csv', sep=';')

df = Cleaner().clean(df)
Visualizer().visualise(df)

X = df.drop('cardio', axis=1)
y = df['cardio']

print(X.shape)
print(X.columns)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

tm = TrainModel()
em = EvaluateModel()

scaler = StandardScaler()
X_train_sc = pd.DataFrame(
    scaler.fit_transform(X_train),
    columns=X_train.columns,
    index=X_train.index
)

X_test_sc = pd.DataFrame(
    scaler.transform(X_test),
    columns=X_test.columns,
    index=X_test.index
)

# 1. Logistic regression
lr = tm.train_logistic(X_train_sc, y_train)
lr_pred = lr.predict(X_test_sc)
em.evaluation(y_test, lr_pred)

# 2. Random Forest
rf = tm.train_rf(X_train_sc, y_train)
rf_pred = rf.predict(X_test_sc)
em.evaluation(y_test, rf_pred)

# 3. Neural Network
nn = tm.train_nn(X_train_sc, y_train, X_test_sc, y_test)
nn_pred = (nn.predict(X_test_sc) > 0.5).astype(int)
em.evaluation(y_test, nn_pred)

# The neural network has highest accuracy (74) so we will use it to predict the patient's risk

nn.save("cardio_nn.keras")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(list(X_train.columns), "feature_columns.pkl")
