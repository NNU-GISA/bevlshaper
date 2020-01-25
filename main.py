# Import dependencies
from exploreKITTI.explore_kitti_lib import *
from adaptive_segmentation import *
import numpy.matlib
from pcl_filter import *

# Constants
ORIGIN_X = 0
ORIGIN_Y = 0
ORIGIN_CIRCLE_RADIUS = 6.1
PATCH_X = -18
PATCH_Y = -10.5
PATCH_WIDTH = 80
PATCH_HEIGHT = 21

# Choose input data
date = '2011_09_26'
drive = '0001'

# Load dataset
dataset = load_dataset(date, drive)
dataset = list(dataset.velo)

# Get PCL from frame function
def get_pcl_from_frame(dataset, frame, points = 0.1):
    points_step = int(1. / points)
    point_size = 0.01 * (1. / points)
    velo_range = range(0, dataset[frame].shape[0], points_step)
    velo_frame = dataset[frame][velo_range, :]
    # velo_frame = velo_frame[:, [0, 1, 2]]
    return velo_frame

# Get PCL data
for frame in range(len(dataset)):
    # Filter point cloud
    velo_frame = get_pcl_from_frame(dataset, frame)
    velo_frame = filter_ground_plane(velo_frame)
    velo_frame = apply_circular_mask(velo_frame, [ORIGIN_X, ORIGIN_Y], ORIGIN_CIRCLE_RADIUS)
    velo_frame = apply_rectangular_mask(velo_frame, [PATCH_X, PATCH_Y], PATCH_WIDTH, PATCH_HEIGHT)

    # Get data
    pcl = list(np.asarray(velo_frame[:, [0, 1]]))

    # Adaptively segment PCL data
    c = cluster_kdtree(pcl, np.matlib.repmat(0.2, 1, len(pcl))[0])
    print(c)