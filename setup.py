from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='scales.py',
    version='0.1.4',
    description='A tool to generate stringed instrument visual aids',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zedchance/scales',
    author='Zed Chance',
    author_email='zedchance@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='music guitar matplotlib',
    py_modules=["scales"],
    python_requires='>=3.7',
    install_requires=['matplotlib', 'numpy'],
)
