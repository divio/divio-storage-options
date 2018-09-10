from setuptools import setup, find_packages
from divio_storage_options import __version__


setup(
    name='divio-storage-options',
    version=__version__,
    description=open('README.rst').read(),
    author='Divio AG',
    author_email='info@divio.com',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=[
        'yurl',
    ],
    include_package_data=True,
    zip_safe=False,
)
