import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="secret-split",
    version="0.0.1",
    author="Daniil F.",
    author_email="mail@...",
    description="Secret splitting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daniil-berg/secret-split",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
