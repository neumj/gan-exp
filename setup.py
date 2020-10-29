from setuptools import setup, find_packages

reqs = [
    "h5py",
    "jupyterlab",
    "matplotlib",
    "numpy",
    "pandas",
    "pillow",
    "scipy",
    "scikit-learn",
    "yaml",
    "imageio",
    "tensorflow",
    "keras",
    "pydot",
    "tqdm"
]

conda_reqs = [
    "h5py",
    "jupyterlab",
    "matplotlib",
    "numpy",
    "pandas",
    "pillow",
    "scipy",
    "scikit-learn",
    "yaml",
    "imageio",
    "tensorflow",
    "keras",
    "pydot",
    "tqdm"
]

test_pkgs = []

setup(
    name="ganexp",
    python_requires='>3.4',
    description="GAN Experiments",
    url="https://github.com/neumj/ganexp",
    install_requires=reqs,
    conda_install_requires=conda_reqs,
    test_requires=test_pkgs,
    packages=find_packages(),
    include_package_data=True
)
