from setuptools import setup

setup(
    name='ipnotify',
    version='0.2',
    url='https://github.com/siso/ipnotify',
    author='Simone Soldateschi',
    author_email='simone.soldateschi@gmail.com',
    license='LICENSE',
    packages=['ipnotify'],
    description='notify when IP address changes',
    long_description=str(open('README.rst', 'rb').read()),
    entry_points={
        'console_scripts': [
            'ipnotify = ipnotify.main:main',
        ]
    },  
    classifiers=(
        'Development Status :: 0.1 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ),
#     install_requires=[
#         "pygame >= 1.9",
#     ],
#    package_data={'pyasteroids': ['data/sounds/*', 'data/fonts/*']}
)
