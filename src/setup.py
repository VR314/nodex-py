from setuptools import find_packages, setup

with open("requirements.txt") as f:
    install_requires = f.read()

setup(
    name="nodex",
    version="1.0",
    description="Test CLI",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "nodex = nodex.cli.main:main",
        ],
    },
    author="VR",
    author_email="",
    url="",
    install_requires=install_requires,
    python_requires=">=3.10"
)
