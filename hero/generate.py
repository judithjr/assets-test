from PIL import Image
import shutil

# Input image file
input_image_path = "astronaut-pattie.png"

# Output directory
output_directory = "sequence"

# Create the output directory if it doesn't exist
shutil.os.makedirs(output_directory, exist_ok=True)

# Number of times to duplicate the image
num_duplicates = 69

# Duplicate the image
for i in range(1, num_duplicates + 1):
    # Open the input image
    with Image.open(input_image_path) as img:
        # Save the duplicated image with a numbered filename
        output_path = f"{output_directory}/{i}.png"
        img.save(output_path)

print(f"{num_duplicates} images duplicated and saved in the '{output_directory}' directory.")
