# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='django-tinkoff-merchant',
    version='1.0',
    author='Oleg K',
    author_email='nameoff.nv@gmail.com',
    packages=['django_tinkoff_merchant'],
    url='https://github.com/nameoffnv/django-tinkoff-merchant',
    license='MIT',
    description='Tinkoff merchant integration',
    install_requires=['django>=2.0.0', 'requests>=2.0.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ]
)