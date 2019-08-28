import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="megadepth",
    version="0.0.1",
    author="Zhengqi Li",
    description="Single-View Depth Prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhengqili/MegaDepth",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)