import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'flask>=1.0.2',
    'gunicorn>=19.9.0'
]

setuptools.setup(
    name="doge-stream-helper",
    version="0.1.0",
    author="Brenden Matthews",
    author_email="brenden@diddyinc.com",
    description="Flask tool for managing Doge stream",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brndnmtthws/doge-stream-helper",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ),
    python_requires=">=3.7",
    install_requires=requires,
)
