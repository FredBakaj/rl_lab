import setuptools

setuptools.setup(
    name="rl_lab",
    version="0.1.0",
    author="Fred",
    author_email="fredbakai@gmail.com",
    description="",
    long_description='',
    long_description_content_type="text/markdown",
    url="https://github.com/FredBakaj/rl_lab",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"],
    python_requires='>=3.6',
    install_requires=["tensorflow==2.3.1", "scikit-learn==0.23.0", "matplotlib", "gym[atari]==0.17.1",
                      "dataclasses", "tqdm", "seaborn", "joblib", "numpy", "coverage", "mock", "opencv-python",
                      "joblib"])
