# -*- coding: utf-8 -*-
"""
rsr-calculator.

-----
It is a package of a calculator to realize observation time
-----
Save in a calculator_test.py:
.. code:: python
    from rsr_calculator import RSR

    if __name__ == "__main__":
        mode_1 = RSR(1)
        print(mode_1.validate_frequency(100))
        print(mode_1.calculator(92, 25, 'mk'))
        print(mode_1.calculator(92, 25, 'mjy'))

        mode_2 = RSR(2)
        print(mode_2.validate_frequency(140))
        print(mode_2.calculator(92, 0.6292637454966844, 'temperature'))
        print(mode_2.calculator(92, 1.7682311248456835, 'flux'))


And Easy to Setup
`````````````````
And run it:
.. code:: bash
    $ pip install git+https://github.com/Ryszard-Ps/rsr-calculator.git
    $ python calculator_test.py

  <https://github.com/Ryszard-Ps/rsr-calculator.git>`_
"""

# Always prefer setuptools over distutils
from setuptools import find_packages, setup

setup(
    name='rsr_calculator',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.3.0',

    description='RSR Integration Time Calculator',
    long_description='long description',

    # The project's main homepage.
    url='https://github.com/Ryszard-Ps/rsr-calculator.git',

    # Author details
    author='Ryszard-Ps',
    author_email='hello@rjbits.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],


    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[''],

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'rsr_calculator': ['package_data.dat'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.

)
