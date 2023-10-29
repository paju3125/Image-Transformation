import cv2
import numpy as np
import streamlit as st

# Create a Streamlit app
st.title('Image Transformations')

# Add an image upload option
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_image is not None:
    image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)
else:
    st.write("Please upload an image.")

# Transformation options in the sidebar
transformation = st.sidebar.radio("Select Transformation", ("Original", "Translation", "Rotation", "Scaling", "Shearing"))

# Apply and display the selected transformation
if transformation == "Original" and uploaded_image is not None:
    st.image(image, caption='Original Image', use_column_width=True, channels="BGR")
elif uploaded_image is not None:
    if transformation == "Translation":
        translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])  # Translate 100 pixels right and 50 pixels down
        transformed_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
    elif transformation == "Rotation":
        rotation_angle = 30  # Rotate 30 degrees
        rotation_matrix = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), rotation_angle, 1)
        transformed_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
    elif transformation == "Scaling":
        scaling_matrix = np.float32([[1.2, 0, 0], [0, 0.8, 0]])  # Scale horizontally by 1.2 times and vertically by 0.8 times
        transformed_image = cv2.warpAffine(image, scaling_matrix, (image.shape[1], image.shape[0]))
    elif transformation == "Shearing":
        shearing_matrix = np.float32([[1, 0.2, 0], [0.2, 1, 0]])  # Apply shear transformation
        transformed_image = cv2.warpAffine(image, shearing_matrix, (image.shape[1], image.shape[0]))
    
    st.image(transformed_image, caption=f'{transformation} Image', use_column_width=True, channels="BGR")
