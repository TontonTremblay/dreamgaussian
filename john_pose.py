import numpy as np
from icecream import ic 
# Define the camera matrices
cam1 = np.array([
    [-0.8353526592254639, -0.41773515939712524, 0.3573281168937683, 1.4404358863830566],
    [0.5497145652770996, -0.6347951889038086, 0.5429999232292175, 2.1889028549194336],
    [1.4901161193847656e-08, 0.6500248908996582, 0.7599128484725952, 3.0633068084716797],
    [0.0, 0.0, 0.0, 1.0]
])

cam2 = np.array([
    [-0.3694077134132385, 0.3430904150009155, -0.863612711429596, -3.4813342094421387],
    [-0.9292674660682678, -0.13638724386692047, 0.3433082401752472, 1.3839198350906372],
    [7.450580596923828e-09, 0.9293478727340698, 0.3692052364349365, 1.488313913345337],
    [0.0, 0.0, 0.0, 1.0]
])

new1 = np.array([
    [1., 0., 0., 0.],
    [0., 1., 0., 0.],
    [0., 0., 1., 2.],
    [0., 0., 0., 1.]
])

# Calculate the relative transformation between cam2 and cam1
relative_transformation = np.linalg.inv(cam1) @ cam2

# Extract the translation part of new1
translation_part_new1 = new1[:3, 3]
translation_part_new1 = [0,0,0]
# Modify the relative transformation to keep the same translation as new1
relative_transformation[:3, 3] = translation_part_new1

# Calculate new2 by applying the modified relative transformation to new1
new2 = relative_transformation @ new1

# Print the resulting new2 matrix
ic(new2)

# Extract the translation component of the transformation matrix
center = np.array([0,0,0])
translation = new2[:3, 3]

# Calculate the distance to the center of the scene
distance = np.linalg.norm(translation - center)

ic(distance)