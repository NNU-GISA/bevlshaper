# Import dependencies
from exploreKITTI.explore_kitti_lib import *
from adaptive_segmentation import *
import numpy.matlib

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
    # Extract PCL data from frame, use X-Y coordinates (BEV)
    pcl = list(np.asarray(get_pcl_from_frame(dataset, frame)[:, [0, 1]]))
    # Adaptively segment PCL data
    c = cluster_kdtree(pcl, np.matlib.repmat(1, 1, len(pcl))[0])
    print(c)