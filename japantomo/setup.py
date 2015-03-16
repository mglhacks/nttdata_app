# -*- coding: utf-8 -*-

from setuptools import setup

project = "japantomo"

setup(
    name=project,
    version='0.1',
    url='https://github.com/imwilsonxu/japantomo',
    description='Fbone (Flask bone) is a Flask (Python microframework) template/bootstrap/boilerplate application.',
    author='Wilson Xu',
    author_email='imwilsonxu@gmail.com',
    packages=["japantomo"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=0.10.1',
        'Flask-SQLAlchemy',
        'Flask-WTF',
        'Flask-Script',
        'Flask-Babel',
        'Flask-Testing',
        'Flask-Mail',
        'Flask-Cache',
        'Flask-Login',
        'Flask-OpenID',
        'nose',
        'mysql-python',
        'fabric',
    ],
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries'
    ]
)
