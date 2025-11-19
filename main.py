import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tensorflow.keras.callbacks import LambdaCallback
from data import generate_image_dataset

X, y = generate_image_dataset()
RANDOM_SEED = 1242
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=RANDOM_SEED)

model = Sequential([
    Dense(8, activation='relu', input_shape=(64,)),
    Dense(8, activation='relu'),
    Dense(3, activation='softmax')
])

model.compile(optimizer=Adam(),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10)

model.evaluate(X_test, y_test)

print(model.evaluate(X_test, y_test))