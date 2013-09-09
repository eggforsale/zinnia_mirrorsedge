"""Setup script for zinnia-theme-bootstrap"""
from setuptools import setup
from setuptools import find_packages

import zinnia_bootstrap

setup(
    name='zinnia-mirrorsedge',
    version=zinnia_mirrorsedge.__version__,

    description='Django Blog Zinnia Mirror\'s Edge theme for django-blog-zinnia',
    long_description=open('README.rst').read(),

    keywords='django, blog, weblog, zinnia, theme, skin, bootstrap, mirrors edge',

    author=zinnia_mirrorsedge.__author__,
    author_email=zinnia_mirrorsedge.__email__,

    packages=find_packages(),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=zinnia_mirrorsedge.__license__,
    include_package_data=True,
    zip_safe=False
)