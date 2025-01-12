# This is the model_training.py

import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping


class SignModel:
    def __init__(self, input_shape=(64, 64, 3),
                 num_classes=29):  # This response the available class, A-Z, nothing, space, and delete
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.model = self.develop_model()

    def develop_model(self):
        # determine the input layer shape
        model = tf.keras.Sequential([
            layers.Input(shape=self.input_shape),  # shrink the images
            layers.Conv2D(32, 3, activation='relu'),

            layers.MaxPooling2D(),  # reduce more of the dimensions
            layers.Conv2D(64, 3, activation='relu'),

            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, activation='relu'),

            layers.MaxPooling2D(),
            layers.Flatten(),

            layers.Dense(64, activation='relu'),
            layers.Dense(self.num_classes, activation='softmax')
        ])

        model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )

        return model


def main():
    # Dataset path
    DATASET_PATH = r'E:\Documents\King Of The Software Engineers\ML\DATA 5100 Programming for Data Science\Final Porject\archive\asl_alphabet_train\asl_alphabet_train'
    MODEL_SAVE_PATH = os.path.join(os.path.dirname(DATASET_PATH), 'best_sign_language_model.keras')

    # Data augmentation and preprocessing
    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        validation_split=0.2
    )

    # Display Class options
    print(f"The options classes: {sorted(os.listdir(DATASET_PATH))}")

    # Prepare data
    train_generator = train_datagen.flow_from_directory(
        DATASET_PATH,
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical',
        subset='training',
        shuffle=True
    )

    validation_generator = train_datagen.flow_from_directory(
        DATASET_PATH,
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical',
        subset='validation',
        shuffle=True
    )

    # Initialize the model
    sign_model = SignModel(num_classes=len(os.listdir(DATASET_PATH)))

    checkpoint = ModelCheckpoint(
        MODEL_SAVE_PATH,
        monitor='val_accuracy',
        save_best_only=True
    )

    early_stopping = EarlyStopping(
        monitor='val_loss',
        patience=10,
        restore_best_weights=True
    )

    # traning the model
    history = sign_model.model.fit(
        train_generator,
        validation_data=validation_generator,
        epochs=50,
        callbacks=[checkpoint, early_stopping]
    )

    # display evaluation
    final_accuracy = history.history['accuracy'][-1]
    final_val_accuracy = history.history['val_accuracy'][-1]
    print(f"\nModel training is now complete!")
    print(f"The training accuracy: {final_accuracy:.4f}")
    print(f"The validation accuracy: {final_val_accuracy:.4f}")


if __name__ == '__main__':
    main()
