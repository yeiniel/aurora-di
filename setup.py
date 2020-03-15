import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aurora-di",  # Replace with your own username
    version="0.0.1",
    author="Yeiniel Suarez Sosa",
    author_email="yeiniel@gmail.com",
    description="Aurora Dependency Injection utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yeiniel/aurora-di",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[],
    extras_require={
        "development": ["nose", "sphinx", "flake8"]
    }
)
