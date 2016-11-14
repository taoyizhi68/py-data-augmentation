try:
    from setuptools import setup
except:
    from distutils.core import setup
 
install_requires = [
    "numpy>=1.10.4",
    "scikit-image>=0.12.3"
]

PACKAGES = ['pydaag',]

setup(
    name = 'pydaag',
    version = '0.0.1',
    description = 'python image data augmentation',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = '',
    author = 'Yizhi Tao',
    author_email = 'see github',
    url = 'https://github.com/taoyizhi68/py-data-augmentation',
    license = 'MIT',
    packages = PACKAGES,
    include_package_data=True,
    zip_safe=True,
    install_requires = install_requires
)