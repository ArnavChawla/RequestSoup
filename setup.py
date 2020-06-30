from setuptools import setup
with open("README.MD","r") as fh:
    long = fh.read()
setup(
    name = 'RequestSoup',
    version='0.0.4',
    description='A wrapper created to make using requests and BeautifulSoup in conjunction easier',
    long_description=long,
    long_description_content_type="text/markdown",
    url = "https://github.com/ArnavChawla/RequestSoup",
    py_modules=["RequestSoup"],
    package_dir={'':'src'},
    install_requires = [
        "requests",
        "bs4"
    ],
)
