import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def visualize_images(directory):
    # Get all image file names in the directory
    image_files = [
        file
        for file in os.listdir(directory)
        if file.endswith((".jpg", ".jpeg", ".png",".PNG"))
    ]

    # Calculate the number of rows and columns for the grid
    num_images = len(image_files)
    num_cols = int(num_images**0.5)
    num_rows = (num_images // num_cols) + int(num_images % num_cols > 0)

    # Set up the figure and subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 12))

    # Iterate over image files and display them in the subplots
    for i, file in enumerate(image_files):
        img_path = os.path.join(directory, file)
        image = mpimg.imread(img_path)

        axes.flatten()[i].imshow(image)
        axes.flatten()[i].axis("off")

        # Add the file name as a text annotation
        filename = os.path.splitext(file)[0]
        axes.flatten()[i].text(
            0.5,
            -0.1,
            filename,
            transform=axes.flatten()[i].transAxes,
            fontsize=8,
            ha="center",
            color="white",
            backgroundcolor="black",
        )

    # Remove any empty subplots
    if num_images < len(axes.flatten()):
        for j in range(num_images, len(axes.flatten())):
            fig.delaxes(axes.flatten()[j])

    # Show the grid of images
    plt.tight_layout()
    plt.savefig("TESTview.png")


# Specify the directory containing the images
image_directory = "test"

# Call the function to visualize the images
visualize_images(image_directory)
