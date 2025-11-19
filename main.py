import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tensorflow.keras.callbacks import LambdaCallback
from data import generate_image_dataset, display_images
import random
from random import randint


X, y = generate_image_dataset()
RANDOM_SEED = 1242
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=RANDOM_SEED)

model = Sequential([
    Dense(8, activation='relu', input_shape=(64,)),
    Dense(8, activation='relu'),
    # Dense(8, activation='relu'),
    Dense(4, activation='softmax')

])

model.compile(optimizer=Adam(learning_rate=0.01),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10)

# model.evaluate(X_test, y_test)

# print(model.evaluate(X_test, y_test))
# display_images(X_test)

def get_random_image():
    digits = []
    while len(digits) < 64:
        digit = random.randint(0, 1)
        digits.append(digit)
    array = np.array(digits, dtype=int)
    
    return array  
image = get_random_image()

print(model.predict(image.reshape(1, 64)))



