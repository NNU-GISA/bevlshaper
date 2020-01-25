# Import dependencies
from exploreKITTI.explore_kitti_lib import *

# Render 2D bird's-eye-view scene from PCL data
def render_2Dbev(frame, dataset, tracklet_rects, tracklet_types, points=0.4):
    # Init figure, define points
    f = plt.figure(figsize=(12, 8))
    axis = f.add_subplot(111, xticks=[], yticks=[])
    points_step = int(1. / points)
    point_size = 0.01 * (1. / points)
    
    # Select data
    dataset_velo = list(dataset.velo)
    velo_range = range(0, dataset_velo[frame].shape[0], points_step)
    velo_frame = dataset_velo[frame][velo_range, :]

    # Draw scatter plot
    axis.scatter(*np.transpose(velo_frame[:, [0, 1]]), s=point_size, c=velo_frame[:, 3], cmap='gray')
    axis.set_xlim(*axes_limits[0])
    axis.set_ylim(*axes_limits[1])
    
    # Save frame and close plot
    filename = 'video/frame_{0:0>4}.png'.format(frame)
    plt.savefig(filename)
    plt.close(f)
    return filename

# Choose input data
date = '2011_09_26'
drive = '0001'

# Load dataset
dataset = load_dataset(date, drive)

# Load tracklets (rects and types)
tracklet_rects, tracklet_types = load_tracklets_for_frames(len(list(dataset.velo)), 'data/{}/{}_drive_{}_sync/tracklet_labels.xml'.format(date, date, drive))

# Render frames animation
frames = []
n_frames = len(list(dataset.velo))
print('Preparing animation frames...')
for frame in range(n_frames):
    print_progress(frame, n_frames - 1)
    filename = render_2Dbev(frame, dataset, tracklet_rects, tracklet_types)
    frames += [filename]
print('...Animation frames ready.')
clip = ImageSequenceClip(frames, fps=5)

# Store animation
clip.write_gif('pcl_data.gif', fps=5)