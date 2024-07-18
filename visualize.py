import cv2
import os
import sys
import matplotlib.pyplot as plt
import math
import random

def visualize_dataset(data_dir):
    """
    Visualize images from the dataset stored as .ppm files.
    The dataset is organized with 43 category directories, each containing .ppm files.
    """
    # Get the list of category directories
    categories = os.listdir(data_dir)
    categories = sorted(categories, key=lambda x: int(x))

    # Calculate the grid dimensions

    num_categories = len(categories)
    grid_cols = math.ceil(math.sqrt(num_categories))
    grid_rows = math.ceil(num_categories / grid_cols)

    # Create the figure and subplots
    fig, axs = plt.subplots(grid_rows, grid_cols, figsize=(12, 12))
    fig.tight_layout(pad=0.5)

    # Iterate over each category directory
    for i, category in enumerate(categories):
        category_dir = os.path.join(data_dir, category)

        # Get the list of .ppm files in the category directory
        files = os.listdir(category_dir)

        # Select a random image from the category
        file_name = random.choice(files)
        file_path = os.path.join(category_dir, file_name)

        # Read and display the image
        image = cv2.imread(file_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Determine the subplot position
        row = i // grid_cols
        col = i % grid_cols

        # Plot the image in the corresponding subplot
        axs[row, col].imshow(image)
        axs[row, col].set_title(f"Category: {category}")
        axs[row, col].axis("off")

    # Hide empty subplots
    for i in range(num_categories, grid_rows * grid_cols):
        row = i // grid_cols
        col = i % grid_cols
        axs[row, col].axis("off")

    plt.savefig("Preview.png")


def main():
    
    visualize_dataset('gtsrb')


if __name__ == "__main__":
    main()
