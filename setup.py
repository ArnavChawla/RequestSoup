from setuptools import setup

setup(
    name = 'Request-Soup',
    version='0.0.1',
    description='A wrapper created to make using requests and BeautifulSoup in conjunction easier',
    py_modules=["manager"],
    package_dir={'':'src'},
)
