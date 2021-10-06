
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wordbook",
    version="0.0.1",
    author="Martin Mena",
    author_email="martinmena@outlook.com",
    description="Translate text or find definitions for single words",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrcrow85/python-wordbook",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=["googletrans", "nltk"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['wordbook=wordbook.translate:main'],
    }
)