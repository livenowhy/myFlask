#!/usr/bin/env python
# encoding: utf-8

"""
@version: 0.1
@author: liuzhangpei
@contact: livenowhy@hotmail.com
@file: setup.py
@time: 2016/6/30 13:52
"""

from setuptools import setup

setup(
    name='Flask',
    version='0.1',
    url='http://github.com/mitsuhiko/flask/',
    license='BSD',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    description='A microframework based on Werkzeug, Jinja2 and good intentions',
    long_description=__doc__,
    py_modules=['flask'],
    zip_safe = False,
    platforms='any',
    install_requires=[
        'Werkzeug>=0.6.1',
        'Jinja2>=2.4'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]

)
