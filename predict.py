import cv2
import numpy as np
import tensorflow as tf
import os

IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43


def predict_image(image_path, model):
    """
    Predict the category label for an input image using the trained model.
    """
    # Load and preprocess the image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT), interpolation=cv2.INTER_AREA)
    img = img.reshape(1, IMG_WIDTH, IMG_HEIGHT, 3)
    img = img.astype("float32") / 255.0

    # Perform prediction
    predictions = model.predict(img)
    predicted_label = np.argmax(predictions)

    return predicted_label


# Load the trained model
model = tf.keras.models.load_model("model.h5")

# Folder path containing the images
folder_path = "test"

# List all the image files in the folder
image_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".jpg")]

# Perform prediction for each image
for image_file in image_files:
    # Perform prediction
    predicted_label = predict_image(image_file, model)

# Print the predicted label for each image
    print(f"Image: {image_file}, Predicted Label: {predicted_label}")