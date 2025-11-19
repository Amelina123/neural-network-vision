import numpy as np
import random

def generate_blank():
    array = np.zeros((8, 8), dtype=int)
    return array

generate_blank()


def generate_horizontal_line():
    array = np.zeros((8, 8), dtype=int)
    random_row = random.randint(0,7)
    array[random_row] = 1

    return array

generate_horizontal_line()


def generate_vertical_line():
    array = np.zeros((8, 8), dtype=int)
    random_column = random.randint(0,7)
    for row in array:
        row[random_column]=1
    return array
generate_vertical_line()

def generate_image_dataset(samples_per_class=100):
    label_images = [(generate_blank, 0),(generate_horizontal_line, 1),(generate_vertical_line, 2)]
    X_list = []
    y_list = []

    for func, label in label_images:
        for i in range(samples_per_class):
           array = func()
           flat_array = array.flatten()
           X_list.append(flat_array)
           y_list.append(label)
    X = np.array(X_list)
    y = np.array(y_list)

    
    return X, y
X,y = generate_image_dataset(3)
# print(X[0].reshape(8, 8))
# print(X[3].reshape(8, 8))
# print(X[6].reshape(8, 8))

