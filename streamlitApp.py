import cv2
import numpy as np
import streamlit as st

# Load an image
image = cv2.imread('charlie.jpeg')

# Set the desired width and height for the output images
output_width = 800
output_height = 600

# Resize the original image to match the output dimensions
image = cv2.resize(image, (output_width, output_height))

# Define the transformation matrix for each operation

# Translation
def apply_translation(image):
    translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])  # Translate 100 pixels right and 50 pixels down
    return cv2.warpAffine(image, translation_matrix, (output_width, output_height))

# Rotation
def apply_rotation(image):
    rotation_angle = 30  # Rotate 30 degrees
    rotation_matrix = cv2.getRotationMatrix2D((output_width / 2, output_height / 2), rotation_angle, 1)
    return cv2.warpAffine(image, rotation_matrix, (output_width, output_height))

# Scaling
def apply_scaling(image):
    scaling_matrix = np.float32([[1.2, 0, 0], [0, 0.8, 0]])  # Scale horizontally by 1.2 times and vertically by 0.8 times
    return cv2.warpAffine(image, scaling_matrix, (output_width, output_height))

# Shearing
def apply_shearing(image):
    shearing_matrix = np.float32([[1, 0.2, 0], [0.2, 1, 0]])  # Apply shear transformation
    return cv2.warpAffine(image, shearing_matrix, (output_width, output_height))

# Create a Streamlit app
st.title('Image Transformations')

# Display the original image
st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption='Original Image', use_column_width=True)

# Transformation options
selected_transformation = st.radio("Select Transformation", ("Translation", "Rotation", "Scaling", "Shearing"))

# Apply and display the selected transformation
if selected_transformation == "Translation":
    transformed_image = apply_translation(image)
elif selected_transformation == "Rotation":
    transformed_image = apply_rotation(image)
elif selected_transformation == "Scaling":
    transformed_image = apply_scaling(image)
else:
    transformed_image = apply_shearing(image)

# Display the transformed image
st.image(cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB), caption=f'{selected_transformation} Image', use_column_width=True)
