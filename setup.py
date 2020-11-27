"""
PZEM distribution file.
"""
from setuptools import setup

setup(
    name='pzem',
    version='0.1.0',
    package_dir={'':'src'},
    packages=['pzem'],
    description='PZEM - Peacefair energy meter data logger',
    url='https://github.com/grzes71/PZEM',
    author='Grzegorz Kotarski',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='argparse cli pzem',
    install_requires=[
          'pyserial',
      ],
)