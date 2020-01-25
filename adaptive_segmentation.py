# Load dependencies
from exploreKITTI.utilities import *
import numpy as np

# Find all points in range function
def find_all_points_in_range(p, r, pcl):
    p_in_range = []
    for n in range(len(pcl)):
        p_tmp = pcl[n]
        if not np.array_equal(p_tmp, p) and np.linalg.norm(p_tmp - p) <= r[n]:
            p_in_range.append(p_tmp)
    return np.asarray(p_in_range)

# Ignore points from point cloud
def ignore_points_from_array(pcl, points):
    pcl_subset = pcl
    for point in points:
        ind = 0
        size = len(pcl_subset)
        while ind != size and not np.array_equal(pcl_subset[ind], point):
            ind += 1
        if ind != size:
            pcl_subset_tmp = []
            for i in range(len(pcl_subset)):
                if i != ind:
                    pcl_subset_tmp.append(pcl_subset[i])
            pcl_subset = pcl_subset_tmp
    return pcl_subset

# Better isin function
def better_isin(points, point):
    if len(points) == 0:
        return False
    else:
        for point_ref in points:
            if np.array_equal(point_ref, point):
                return True

# Cluster K-D tree function
def cluster_kdtree(pcl, a):
    # Init empty set of clusters
    clusters = []
    # Init empty list of checked points
    checked_p = []
    # Iterate over all points p
    for n in range(len(pcl)):
        # Print progress
        print("Iteration", n, "out of", len(pcl))
        # Select point p
        p = pcl[n]
        # If point p was not considered yet, continue
        if not better_isin(checked_p, p):
            cluster = [p]
            # Iterate along cluster
            k = 0
            # Iterate over cluster while it is created to extend it
            while k < len(cluster):
                # Print progress
                print_progress(k + 1, len(cluster))
                # Attach iterate over cluster, select last added point
                p_tmp = cluster[k]
                # Set constant radius
                # TODO - Make it relative to considered point to compensate resolution differences
                r = a
                # Select all points in range r from current point p
                ps_in_range = find_all_points_in_range(p_tmp, r, ignore_points_from_array(pcl, cluster))
                # Check if any point is in range
                if ps_in_range.size > 0:
                    # Extend current cluster by new point
                    cluster = np.concatenate((cluster, ps_in_range), axis=0)
                # Add point to checked points
                checked_p.append(p_tmp)
                k += 1
            # Append complete cluster to set of clusters
            clusters.append(cluster)
    # Return set of clusters
    return clusters