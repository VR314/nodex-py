from setuptools import setup

setup(
    name="Nodex",
    version="0.0",
    description="Test CLI",
    entry_points={
        "console_scripts": [
            "nodex = cli.main:main",
        ],
    },
    author="VR",
    author_email="",
    url="",
    install_requires=["zmq"],
    python_requires=">=3.10",
)
