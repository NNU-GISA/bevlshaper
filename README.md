### bevlshaper

Algorithm for bird's-eye-view L-shape fitting in 3D LIDAR point clouds from traffic scenarios

![conda](https://img.shields.io/badge/Conda-4.7.5-green.svg)
![python](https://img.shields.io/badge/Python-3.7.3-yellow.svg)
![numpy](https://img.shields.io/badge/NumPy-1.18.1-blue.svg)

---

:hammer: **UNDER DEVELOPMENT** :wrench:

#### Foreword
This project is inspired by the paper [Efficient L-Shape Fitting for Vehicle Detection Using Laser Scanners](https://www.ri.cmu.edu/wp-content/uploads/2017/07/Xiao-2017-Efficient-L-Shape-Fitting.pdf).
As in the paper, a K-D tree algorithm is used for segmentation after point cloud filtering.
This step is inspired by [Moving object classification using horizontal laser scan data](https://www.researchgate.net/profile/Huijing_Zhao/publication/224557150_Moving_object_classification_using_horizontal_laser_scan_data/links/00b7d520b05aa1a131000000/Moving-object-classification-using-horizontal-laser-scan-data.pdf).
Within found clusters, L-shapes are detected.
For easy prototyping and modelling, Python was used instead of a more computationally powerful language.
The NumPy library is heavily used.

#### Prepare environment
```bash
conda create --name kitti -y python=3
conda activate kitti
```

#### Install dependencies
```bash
git clone https://github.com/scud3r1a/exploreKITTI.git
pip install -r requirements.txt
```

#### Run _bevlshaper_ on KITTI dataset scenes
```bash
# Display traffic scene in BEV
python render_scene.py

# Run segmentation and detection algorithm
# See main.py for execution config
python main.py
```