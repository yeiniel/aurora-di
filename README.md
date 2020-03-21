# Aurora Dependency Injection utilities 
[![Documentation Status](https://readthedocs.org/projects/aurora-di/badge/?version=latest)](https://aurora-di.readthedocs.io/en/latest/?badge=latest)

## Installing Package

```bash
pip install -i https://test.pypi.org/simple/ aurora-di
```

## Setting up a Development Environment

To setup a development environment you need to install all dependencies listed
on `extras_require[development]` on `setup.py`. If you already has pipenv 
installed on your system you can automate virtual environment management and
dependency installation using the following commands:

```bash
pipenv install -e .
pipenv install -e .[development]
```

## Building Project Documentation

You can build the project documentation running the following command on the
`docs` directory:

```bash
make html
```

This command will generate a set of html files in the `docs/_build/html` 
folder.