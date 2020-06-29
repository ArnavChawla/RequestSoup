from setuptools import setup

setup(
    name = 'RequestSoup',
    version='0.0.1',
    description='A wrapper created to make using requests and BeautifulSoup in conjunction easier',
    py_modules=["RequestSoup"],
    package_dir={'':'src'},
    install_requires = [
        "requests",
        "bs4"
    ],
)
