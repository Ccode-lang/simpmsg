import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simpmsg", # Replace with your own username
    version="0.0.1",
    author="Ccode-lang",
    author_email="coop112097@gmail.com",
    description="For all the people too lazy too learn to use tcp.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ccode-lang/simpmsg",
    packages=setuptools.find_packages(),
    install_requires = [],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
