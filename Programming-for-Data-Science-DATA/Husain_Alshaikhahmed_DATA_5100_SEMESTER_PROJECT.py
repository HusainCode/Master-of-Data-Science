# this is the collection_data.py

import numpy as np
from sklearn.model_selection import train_test_split
import os
import pandas as pd


# This class is going to prepare the data into a suitable format
# Credit due to : https://www.kaggle.com/datasets/grassknoted/asl-alphabet
def dataset_preparation(
        # this is my local path
        dataset_path=r'E:\Documents\King Of The Software Engineers\ML\DATA 5100 Programming for Data Science\Final '
                     r'Porject'):
    dataset_info = {
        'number_of_images': 0,
        'classes': [],
        'train_split': 0.8,
        'validation_split': 0.2
    }

    # Iterate dataset directory
    for root, dirs, files in os.walk(dataset_path):

        # Counts the number of image files in a directory with the given extensions

        dataset_info['number_of_images'] += len([f for f in files if f.endswith(('.jpg', '.png', '.jpeg'))])
        # # Capture only top directories
        if not dataset_info['classes'] and dirs:
            dataset_info['classes'] = dirs

    return dataset_info


def main():
    # my local path
    DATASET_PATH = (r'E:\Documents\King Of The Software Engineers\ML\DATA 5100 Programming for Data Science\Final '
                    r'Porject\archive\asl_alphabet_train\asl_alphabet_train')
    # Gather and preprocess data
    dataset_information = dataset_preparation(DATASET_PATH)
    print("Data Collection and Preprocessing Summary:")
    print(f"Number of Imges: {dataset_information['number_of_images']}")
    print(f"Available classes: {dataset_information['classes']}")
    print(f" The split: {dataset_information['train_split'] * 100}%")
    print(f"The validation split: {dataset_information['validation_split'] * 100}%")


if __name__ == '__main__':
    main()
