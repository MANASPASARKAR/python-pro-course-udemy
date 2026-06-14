from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

class TrainModel:

    def train_logistic(self, X_train_sc, y_train):
        model = LogisticRegression()
        model.fit(X_train_sc, y_train)
        return model

    def train_rf(self, X_train_sc, y_train):

        model = RandomForestClassifier(
            n_estimators=200,
            max_depth=8, # prevent overfitting
            min_samples_leaf=10 # generalise
        )

        model.fit(X_train_sc, y_train)
        return model

    def train_nn(self, X_train_sc, y_train, X_test_sc, y_test):

        model = Sequential()

        model.add(Dense(50, activation='relu'))
        model.add(Dropout(0.3))

        model.add(Dense(25, activation='relu'))
        model.add(Dropout(0.3))

        model.add(Dense(12, activation='relu'))
        model.add(Dropout(0.3))

        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='adam')

        early_Stop = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=30)

        model.fit(x=X_train_sc, y=y_train, epochs=600, validation_data=(X_test_sc, y_test), callbacks=[early_Stop])
        return model

