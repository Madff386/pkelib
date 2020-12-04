import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pkelib", 
    version="1.0.0",
    author="Mdaff169",
    author_email="dehersbach@gmail.com",
    description="PKE library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Madff386/pkelib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
