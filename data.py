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

def generate_checkboard_image():
    array = np.zeros((8, 8), dtype=int)
    array[1::2, ::2] = 1
    array[::2, 1::2] = 1 
    return array
generate_checkboard_image()


def generate_image_dataset(samples_per_class=100):
    label_images = [(generate_blank, 0),(generate_horizontal_line, 1),(generate_vertical_line, 2), (generate_checkboard_image, 3)]
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

def display_images(X):
    for array in X:
        reshape_array = array.reshape(8,8)
        pretty_array = ["image:\n"]
        # print (reshape_array)
        for line in reshape_array:
            string = "".join(str(x) for x in line)
         
            for i in string:
                if i == '0':
                    pretty_array.append(" ")
                elif i == '1':
                    pretty_array.append("#")
            pretty_array.append("\n")
        final_string = "".join(pretty_array)
        print(final_string)
        


# display_images(X)