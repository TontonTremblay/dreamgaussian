import math
import numpy as np

# Define the array
array = [1.4404358863830566, 2.1889028549194336, 3.0633068084716797]

# Calculate the Euclidean length
euclidean_length = np.sqrt(sum(x**2 for x in array))

print("Euclidean Length:", euclidean_length)