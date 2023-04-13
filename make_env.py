import os

# Define the name of the new environment
env_name = "geospatial"

# Define the required packages
packages = [
    "python=3.8",
    "geos",
    "gdal",
    "tensorflow",
    "keras",
    "pytorch",
    "torchvision",
    "jupyter",
    "ipykernel",
    "rise",
    "matplotlib",
    "numpy",
    "pandas",
    "scikit-learn",
    "scipy",
    "scikit-image",
    "networkx",
    "pysal",
    "geopandas",
    "shapely",
    "fiona",
    "rtree",
    "descartes"
]

# Add the conda-forge and defaults channels
os.system("conda config --add channels conda-forge")
os.system("conda config --add channels defaults")

# Create the environment
os.system(f"conda create -n {env_name} {' '.join(packages)}")

# Activate the environment
os.system(f"conda activate {env_name}")

# Install the missing packages
os.system("conda install -y gdal-devel geos-devel torchtext osgeo otb")

# Register the environment as a kernel for Jupyter notebooks
os.system(f"python -m ipykernel install --user --name {env_name} --display-name {env_name}")

# Deactivate the environment
os.system("conda deactivate")
