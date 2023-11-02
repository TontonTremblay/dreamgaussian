import json
import numpy as np

# Load the JSON file
with open('zhenggang/data_DreamG/6802359bdc16486083301bea24f1f3f5_9/eval_cam.json', 'r') as file:
    data = json.load(file)

# Initialize the center of the scene
center = np.array([0.0, 0.0, 0.0])

# Iterate through the frames
for frame in data['frames']:
    transform_matrix = np.array(frame['transform_matrix'])
    
    # Extract the translation component of the transformation matrix
    translation = transform_matrix[:3, 3]
    
    # Calculate the distance to the center of the scene
    distance = np.linalg.norm(translation - center)
    
    print(f"Frame: {frame['file_path']}, Distance to Center: {distance}")