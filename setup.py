
import setuptools

setuptools.setup(
    name="aurora-di",
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
    install_requires=[],
    extras_require={
        "development": [
            # dependencies used to build project documentation
            "sphinx"
        ]
    }
)