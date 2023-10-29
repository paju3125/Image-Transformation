import cv2
import numpy as np

# Load an image
image = cv2.imread('static/images/ram.jpg')

# Set the desired width and height for the output images
output_width = 800
output_height = 600

# Resize the original image to match the output dimensions
image = cv2.resize(image, (output_width, output_height))

# Define the transformation matrix for each operation
# 1. Translation
translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])  # Translate 100 pixels right and 50 pixels down

# 2. Rotation
rotation_angle = 30  # Rotate 30 degrees
rotation_matrix = cv2.getRotationMatrix2D((output_width / 2, output_height / 2), rotation_angle, 1)

# 3. Scaling
scaling_matrix = np.float32([[1.2, 0, 0], [0, 0.8, 0]])  # Scale horizontally by 1.2 times and vertically by 0.8 times

# 4. Shearing
shearing_matrix = np.float32([[1, 0.2, 0], [0.2, 1, 0]])  # Apply shear transformation

# Apply the transformations to the resized image
translated_image = cv2.warpAffine(image, translation_matrix, (output_width, output_height))
rotated_image = cv2.warpAffine(image, rotation_matrix, (output_width, output_height))
scaled_image = cv2.warpAffine(image, scaling_matrix, (output_width, output_height))
sheared_image = cv2.warpAffine(image, shearing_matrix, (output_width, output_height))

# Save the individual transformed images
cv2.imwrite('translated_image.jpg', translated_image)
cv2.imwrite('rotated_image.jpg', rotated_image)
cv2.imwrite('scaled_image.jpg', scaled_image)
cv2.imwrite('sheared_image.jpg', sheared_image)

# Display the canvas with the original and transformed images
canvas = np.vstack((np.hstack((image, translated_image)), np.hstack((rotated_image, scaled_image))))
cv2.imshow('Images with Transformations', canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
