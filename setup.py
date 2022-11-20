from setuptools import find_packages, setup

setup(
    name='lgtm',
    version='1.0.0',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'Click~=8.0',
        'Pillow~=9.3.0',
        'requests~=2.28.0',
    ],
    entry_points={
        'console_scripts': [
            'lgtm=lgtm.core:cli'
        ]
    }
)
