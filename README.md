## bevLshaper
Find L-shapes in 3D point clouds transformed into bird's-eye-view. Designed for vehicle detection in traffic scenarios.
![conda](https://img.shields.io/badge/Conda-4.7.5-green.svg)
![python](https://img.shields.io/badge/Python-3.7.3-yellow.svg)
![numpy](https://img.shields.io/badge/NumPy-1.18.1-blue.svg)
---

:hammer: **================= UNDER DEVELOPMENT =================** :wrench:

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

#### Run bevLshaper on KITTI dataset scenes
```bash
# See main.py for execution config
python main.py
```