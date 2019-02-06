import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyMensa",
    version="1.0.0",
    author="Pascal Schärli",
    author_email="pas.schaerli@sunrise.ch",
    description="A python package for fetching mensa menus at ETH and UNI Zürich",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pasch13/pyMensa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
