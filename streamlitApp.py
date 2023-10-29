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
transformation = st.sidebar.selectbox("Select Transformation", ["Original", "Translation", "Rotation", "Scaling", "Shearing", "Perspective", "Elastic Distortion"])

# Apply and display the selected transformation
if uploaded_image is not None:
    if transformation == "Original":
        st.image(image, caption='Original Image', use_column_width=True, channels="BGR")
    else:
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
        elif transformation == "Perspective":
            pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])  # Source points
            pts2 = np.float32([[10, 100], [200, 50], [100, 250], [200, 200]])  # Destination points
            perspective_matrix = cv2.getPerspectiveTransform(pts1, pts2)
            transformed_image = cv2.warpPerspective(image, perspective_matrix, (image.shape[1], image.shape[0]))
        elif transformation == "Elastic Distortion":
            rows, cols, _ = image.shape
            grid_size = 20
            x, y = np.meshgrid(np.linspace(0, cols, grid_size), np.linspace(0, rows, grid_size))
            x_displace = 10 * np.sin(2 * np.pi * x / cols)
            y_displace = 10 * np.sin(2 * np.pi * y / rows)
            map_x = (x + x_displace).astype(np.float32)
            map_y = (y + y_displace).astype(np.float32)
            transformed_image = cv2.remap(image, map_x, map_y, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
        
        st.image(transformed_image, caption=f'{transformation} Image', use_column_width=True, channels="BGR")
