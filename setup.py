import setuptools

setuptools.setup(
    name="test-package-name",
    version="0.0.13",
    author="none",
    author_email="author@example.com",
    description="desc",
    long_description_content_type="text/markdown",
    entry_points = {
        "console_scripts": ['myimport = pack.main:local_import']
        },
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)