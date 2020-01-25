# Load dependencies
import numpy as np
import math
GROUND_PLANE_REFLECTANCE = 0
GROUND_PLANE_Z_UPPER_BORDER = 0

# Filter ground plane function
def filter_ground_plane(pcl):
    filtered_pcl = []
    for point in pcl:
        if not point[3] < GROUND_PLANE_REFLECTANCE or not point[2] < GROUND_PLANE_Z_UPPER_BORDER:
            filtered_pcl.append(point)
    return np.asarray(filtered_pcl)

# Apply circular mask function
def apply_circular_mask(pcl, origin, r):
    filtered_pcl = []
    for point in pcl:
        if not math.sqrt(math.pow(point[0] - origin[0], 2) + math.pow(point[1] - origin[1], 2)) <= r:
            filtered_pcl.append(point)
    return np.asarray(filtered_pcl)

# Apply rectangular mask function
def apply_rectangular_mask(pcl, patch_init, width, height):
    x = patch_init[0]
    y = patch_init[1]
    filtered_pcl = []
    for point in pcl:
        if not point[0] < x and not point[0] > x + width and not point[1] < y and not point[1] > y + height:
            filtered_pcl.append(point)
    return np.asarray(filtered_pcl)